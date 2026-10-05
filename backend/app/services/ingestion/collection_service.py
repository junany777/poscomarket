from datetime import datetime, timezone
import hashlib

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.entities import CollectionRun, SourceDocument
from app.services.ingestion.collectors.html import HtmlIndexCollector
from app.services.ingestion.collectors.rss import RssCollector
from app.services.ingestion.deduplicator import find_duplicate
from app.services.ingestion.fetcher import HttpFetcher
from app.services.ingestion.normalizer import normalize_item
from app.services.ingestion.registry import enabled_sources, load_sources
from app.services.ingestion.relevance_filter import assess_relevance
from app.services.pipeline import run_intelligence_pipeline
from app.services.dart import DartClient


COLLECTOR_TYPES = {"RSS": RssCollector, "ATOM": RssCollector, "HTML_INDEX": HtmlIndexCollector}


def list_registry_sources() -> list[dict]:
    return [{"source_code": "OPENDART", "source_name": "OpenDART 제조업 공시", "type": "DISCLOSURE", "source_authority": "OFFICIAL", "collector_type": "DART_API", "enabled": True, "default": True, "priority": 0, "language": "ko", "industries": ["MANUFACTURING"]}] + load_sources(settings.news_registry_path)


async def collect_dart_sources(db: Session, dry_run: bool = False) -> dict:
    source_code = "OPENDART"
    run = CollectionRun(source_code=source_code, started_at=datetime.now(timezone.utc), status="RUNNING")
    db.add(run)
    db.commit()
    new_document_ids: list[str] = []
    errors: list[str] = []
    try:
        result = await DartClient().disclosures(page_count=100)
        items = result.get("items", [])
        run.items_seen = len(items)
        for item in items:
            try:
                source_url = item.get("url") or item.get("receipt_no") or ""
                content = f"{item.get('corp_name') or '기업명 확인 필요'} {item.get('report_name') or '공시 제목 확인 필요'}"
                content_hash = hashlib.sha256(source_url.encode("utf-8")).hexdigest()
                if db.scalar(select(SourceDocument).where(SourceDocument.content_hash == content_hash)):
                    run.items_duplicate += 1
                    continue
                if dry_run:
                    run.items_new += 1
                    continue
                document = SourceDocument(source_type="DISCLOSURE", source_name="OpenDART", source_url=source_url, title=f"{item.get('corp_name') or '기업명 확인 필요'} · {item.get('report_name') or '공시 제목 확인 필요'}", published_at=item.get("receipt_date"), collected_at=datetime.now(timezone.utc).isoformat(), content=content, content_hash=content_hash, language="ko", status="READY_FOR_INTELLIGENCE", metadata_json={"source_code": source_code, "provider": "OPENDART", "industry_code": item.get("industry_code"), "industry_name": item.get("industry_name"), "receipt_no": item.get("receipt_no"), "stock_code": item.get("stock_code")})
                db.add(document)
                db.flush()
                new_document_ids.append(document.id)
                run.items_new += 1
            except Exception as exc:
                run.items_failed += 1
                errors.append(str(exc)[:240])
        run.status = "PARTIAL" if errors else "COMPLETED"
    except Exception as exc:
        run.status = "FAILED"
        run.items_failed += 1
        errors.append(str(exc)[:240])
    run.error_summary = "; ".join(errors)[:2000] or None
    run.completed_at = datetime.now(timezone.utc)
    db.commit()
    return {"run_id": run.id, "source_code": run.source_code, "status": run.status, "items_seen": run.items_seen, "items_new": run.items_new, "items_duplicate": run.items_duplicate, "items_failed": run.items_failed, "error_summary": run.error_summary, "source_document_ids": new_document_ids}


async def collect_sources(db: Session, source_codes: list[str] | None = None, dry_run: bool = False) -> list[dict]:
    selected_codes = source_codes if source_codes is not None else ["OPENDART"]
    results = []
    if "OPENDART" in {code.upper() for code in selected_codes}:
        results.append(await collect_dart_sources(db, dry_run=dry_run))
    selected_news_codes = [code for code in selected_codes if code.upper() != "OPENDART"]
    fetcher = HttpFetcher(settings.news_fetch_timeout_seconds, settings.news_fetch_retries, settings.news_max_concurrency)
    registered_sources = load_sources(settings.news_registry_path)
    selected_news_set = {code.upper() for code in selected_news_codes}
    news_sources = [source for source in registered_sources if source.get("source_code", "").upper() in selected_news_set]
    for source in news_sources:
        run = CollectionRun(source_code=source["source_code"], started_at=datetime.now(timezone.utc), status="RUNNING")
        db.add(run)
        db.commit()
        errors: list[str] = []
        new_document_ids: list[str] = []
        try:
            collector_type = source.get("collector_type", "RSS").upper()
            collector_class = COLLECTOR_TYPES[collector_type]
            items = await collector_class(fetcher).collect(source)
            run.items_seen = len(items)
            for raw_item in items:
                try:
                    item = normalize_item(raw_item)
                    relevance = assess_relevance(item.title, item.content, source, settings.news_relevance_threshold)
                    if not relevance.relevant:
                        continue
                    if find_duplicate(db, item):
                        run.items_duplicate += 1
                        continue
                    if dry_run:
                        run.items_new += 1
                        continue
                    document = SourceDocument(source_type=source.get("type", "NEWS"), source_name=source["source_name"], source_url=item.url, title=item.title, published_at=item.published_at, collected_at=datetime.now(timezone.utc).isoformat(), content=item.content, content_hash=item.metadata["content_hash"], language=item.language, status="READY_FOR_INTELLIGENCE", metadata_json={**item.metadata, "source_code": source["source_code"], "collector_type": collector_type, "source_authority": source.get("source_authority", "SECONDARY"), "relevance_score": relevance.score, "matched_keywords": relevance.matched_keywords, "external_id": item.external_id})
                    db.add(document)
                    db.flush()
                    new_document_ids.append(document.id)
                    run.items_new += 1
                except Exception as exc:
                    run.items_failed += 1
                    errors.append(str(exc)[:240])
            run.status = "PARTIAL" if errors else "COMPLETED"
            if settings.auto_run_intelligence and not dry_run:
                for document_id in new_document_ids[: settings.max_auto_intelligence_per_run]:
                    try:
                        run_intelligence_pipeline(db, document_id)
                    except Exception as exc:
                        errors.append(f"intelligence:{document_id}:{str(exc)[:180]}")
                if errors:
                    run.status = "PARTIAL"
        except Exception as exc:
            run.status = "FAILED"
            run.items_failed += 1
            errors.append(str(exc)[:240])
        run.error_summary = "; ".join(errors)[:2000] or None
        run.completed_at = datetime.now(timezone.utc)
        db.commit()
        results.append({"run_id": run.id, "source_code": run.source_code, "status": run.status, "items_seen": run.items_seen, "items_new": run.items_new, "items_duplicate": run.items_duplicate, "items_failed": run.items_failed, "error_summary": run.error_summary, "source_document_ids": new_document_ids})
    return results

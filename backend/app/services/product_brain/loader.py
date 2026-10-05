from pathlib import Path
import os
from threading import RLock

from app.services.product_brain.router import ProductRouteResult


_CACHE: dict[str, tuple[int, str]] = {}
_LOCK = RLock()
_STATS = {"hits": 0, "misses": 0, "files_loaded": 0, "bytes_loaded": 0}


def load_routed_products(route: ProductRouteResult, max_files: int = 3) -> list[dict]:
    """Load only files selected by the deterministic router; never glob the knowledge base."""
    if max_files < 1 or max_files > 3:
        raise ValueError("max_files must be between 1 and 3")
    loaded: list[dict] = []
    root = Path(os.getenv("KNOWLEDGE_ROOT", str(Path(__file__).resolve().parents[4])))
    for relative in route.knowledge_files[:max_files]:
        path = root / relative
        if not path.exists():
            continue
        mtime = path.stat().st_mtime_ns
        with _LOCK:
            cached = _CACHE.get(relative)
            if cached and cached[0] == mtime:
                text = cached[1]
                _STATS["hits"] += 1
            else:
                text = path.read_text(encoding="utf-8")
                _CACHE[relative] = (mtime, text)
                _STATS["misses"] += 1
                _STATS["files_loaded"] += 1
                _STATS["bytes_loaded"] += len(text.encode("utf-8"))
        loaded.append({"path": relative, "content": text})
    return loaded


def product_load_stats(reset: bool = False) -> dict:
    with _LOCK:
        result = dict(_STATS)
        result["cache_hit_rate"] = round(result["hits"] / (result["hits"] + result["misses"]), 4) if result["hits"] + result["misses"] else None
        if reset:
            for key in _STATS: _STATS[key] = 0
        return result

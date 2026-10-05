from app.services.ingestion.normalizer import canonicalize_url, normalize_text
from app.services.ingestion.relevance_filter import assess_relevance
from app.services.ingestion.article_parser import parse_article


def test_url_normalization_removes_tracking_parameters():
    assert canonicalize_url("HTTPS://News.Example/entry/?utm_source=x&id=7#fragment") == "https://news.example/entry?id=7"


def test_text_normalization_collapses_whitespace():
    assert normalize_text("  철강\n\t 수요  ") == "철강 수요"


def test_relevance_is_deterministic_and_explainable():
    result = assess_relevance("EV battery steel demand", "Automotive production is expanding", {"type": "OFFICIAL"}, threshold=2)
    assert result.relevant is True
    assert "steel" in result.matched_keywords
    assert result.score >= 2


def test_html_article_parser_removes_navigation_noise():
    parsed = parse_article("<nav>menu</nav><main><h1>Steel update</h1><p>EV steel demand rises.</p></main>")
    assert parsed["title"] == "Steel update"
    assert "menu" not in parsed["content"]
    assert "EV steel demand" in parsed["content"]

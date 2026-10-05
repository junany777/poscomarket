from dataclasses import dataclass


@dataclass(frozen=True)
class JudgeResult:
    label: str
    score: float
    reason: str


def judge_strategy(*_args, **_kwargs) -> JudgeResult:
    """Extension point for a separately configured evaluator; production output is never self-judged here."""
    return JudgeResult("UNREVIEWED", 0, "LLM judge is disabled until an independent evaluation model is configured.")

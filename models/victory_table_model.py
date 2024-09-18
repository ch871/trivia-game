from dataclasses import dataclass
from datetime import timedelta


@dataclass
class VictoryTable:
    user_id: int
    question_id: int
    answer_text: str
    is_correct: bool
    time_taken: timedelta = None
    id: int = None

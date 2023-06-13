from dataclasses import dataclass


@dataclass
class Currency:
    ticker: str
    value: float
    timestamp: float

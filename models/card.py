from dataclasses import dataclass


@dataclass
class Card:
    name: str
    value: int = 0

from pydantic import BaseModel
from typing import Optional


class MoveCardRequestData(BaseModel):
    card_id: int
    deck_id: int
    position: int


class MoveDeckRequestData(BaseModel):
    deck_id: Optional[int]
    position: int

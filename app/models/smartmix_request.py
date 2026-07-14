from pydantic import BaseModel
from typing import List


class SmartMixRequest(BaseModel):
    mood: str
    favorite_artists: List[str]
    favorite_genres: List[str]
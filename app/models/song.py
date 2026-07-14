from pydantic import BaseModel
from typing import List

class Song(BaseModel):
    id: int
    title: str
    artist: str
    album: str
    genre: str
    mood: List[str]
    duration: int # en secondes
    popularity: float # de 0 à 100
    release_year: int
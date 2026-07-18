from pydantic import BaseModel
from typing import Optional

class Song(BaseModel):
    id: str
    title: str
    artist: str
    duration: Optional[float] = None
    url: Optional[str] = None
    genre: Optional[str] = None
    mood: Optional[str] = None
    tempo: Optional[float] = None
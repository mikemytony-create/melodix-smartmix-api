from pydantic import BaseModel
from typing import Optional, List, Union

class Song(BaseModel):
    id: Union[str, int] # Accepte "1" ou 1
    title: str
    artist: str
    duration: Optional[float] = None
    url: Optional[str] = None
    genre: Optional[str] = None
    mood: Optional[Union[str, List[str]]] = None # Accepte "happy" ou ["happy", "chill"]
    tempo: Optional[float] = None
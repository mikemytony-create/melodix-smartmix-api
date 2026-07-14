from pydantic import BaseModel
from typing import List

class UserProfile(BaseModel):
    favorite_artists: List[str]
    favorite_genres: List[str]
    liked_songs: List[int]
    skipped_songs: List[int]
    recently_played: List[int]
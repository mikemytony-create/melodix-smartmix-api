from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class LyricsUpload(BaseModel):
    song_id: UUID
    artist_id: UUID

    title: str
    language: str

    lyrics: str
    synced_lyrics: Optional[str] = None

    allow_translation: bool = False
    allow_slowed: bool = False


class LyricsUpdate(BaseModel):
    lyrics: str
    synced_lyrics: Optional[str] = None


class LyricsResponse(BaseModel):
    song_id: UUID
    lyrics: Optional[str]
    synced_lyrics: Optional[str]
    language: Optional[str]
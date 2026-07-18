from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class LyricsModel(BaseModel):
    song_id: UUID = Field(default_factory=uuid4)
    artist_id: UUID

    title: str
    language: str

    lyrics: str
    synced_lyrics: Optional[str] = None

    allow_translation: bool = False
    allow_slowed: bool = False

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

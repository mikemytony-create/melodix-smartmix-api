from uuid import UUID, uuid4
from datetime import datetime

from pydantic import BaseModel, Field


class TranslationModel(BaseModel):
    translation_id: UUID = Field(default_factory=uuid4)

    song_id: UUID

    source_language: str
    target_language: str

    translated_lyrics: str

    provider: str = "google"

    version: str = "1.0"

    created_at: datetime = Field(default_factory=datetime.utcnow)

    is_verified: bool = False

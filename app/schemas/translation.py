from uuid import UUID
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TranslationRequest(BaseModel):
    song_id: UUID
    target_language: str = Field(
        ...,
        description="Target language (fr, en, es, pt, sw, ln, ar, yo)"
    )


class TranslationResponse(BaseModel):
    translation_id: UUID
    song_id: UUID

    source_language: str
    target_language: str

    translated_lyrics: str

    provider: str
    version: str

    created_at: datetime

    is_verified: bool


class TranslationUpdate(BaseModel):
    translated_lyrics: Optional[str] = None
    is_verified: Optional[bool] = None

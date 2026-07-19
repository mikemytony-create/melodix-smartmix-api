from uuid import UUID
from pydantic import BaseModel


class AudioGenerateRequest(BaseModel):
    song_id: UUID


class AudioResponse(BaseModel):
    audio_id: UUID
    song_id: UUID

    effect: str
    original_url: str
    generated_url: str
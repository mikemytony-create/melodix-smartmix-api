from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field


class AudioModel(BaseModel):
    audio_id: UUID = Field(default_factory=uuid4)
    song_id: UUID

    effect: str
    original_url: str
    generated_url: str

    created_at: datetime = Field(default_factory=datetime.utcnow)
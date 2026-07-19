from uuid import UUID, uuid4
from datetime import datetime

from pydantic import BaseModel, Field


class CloudFileModel(BaseModel):
    file_id: UUID = Field(default_factory=uuid4)
    song_id: UUID
    artist_id: UUID
    filename: str
    file_type: str
    file_url: str
    file_size: int
    uploaded_at: datetime = Field(default_factory=datetime.utcnow)
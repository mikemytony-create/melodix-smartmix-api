from uuid import UUID
from pydantic import BaseModel


class UploadSongRequest(BaseModel):
    song_id: UUID
    artist_id: UUID
    filename: str
    file_type: str
    file_size: int


class CloudResponse(BaseModel):
    file_id: UUID
    song_id: UUID
    artist_id: UUID
    filename: str
    file_type: str
    file_url: str
    file_size: int
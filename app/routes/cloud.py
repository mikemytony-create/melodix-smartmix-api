from uuid import UUID

from fastapi import APIRouter

from app.schemas.cloud import UploadSongRequest
from app.services.cloud import cloud_service

router = APIRouter()


@router.post("/upload")
def upload_song(request: UploadSongRequest):

    return cloud_service.upload_song(
        song_id=request.song_id,
        artist_id=request.artist_id,
        filename=request.filename,
        file_type=request.file_type,
        file_size=request.file_size,
    )


@router.get("/{file_id}")
def get_file(file_id: UUID):

    return cloud_service.get_file(file_id)


@router.delete("/{file_id}")
def delete_file(file_id: UUID):

    return cloud_service.delete_file(file_id)
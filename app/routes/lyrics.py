from uuid import UUID

from fastapi import APIRouter

from app.schemas.lyrics import (
    LyricsUpload,
    LyricsUpdate,
    LyricsResponse,
)

from app.services.lyrics import lyrics_service

router = APIRouter()


@router.post("/upload", response_model=dict)
def upload_lyrics(payload: LyricsUpload):
    return lyrics_service.upload_lyrics(
        song_id=payload.song_id,
        lyrics=payload.lyrics,
        synced_lyrics=payload.synced_lyrics,
    )


@router.get("/{song_id}", response_model=LyricsResponse)
def get_lyrics(song_id: UUID):
    return lyrics_service.get_lyrics(song_id)


@router.get("/{song_id}/synced", response_model=LyricsResponse)
def get_synced_lyrics(song_id: UUID):
    return lyrics_service.get_synced_lyrics(song_id)


@router.put("/{song_id}", response_model=dict)
def update_lyrics(song_id: UUID, payload: LyricsUpdate):
    return lyrics_service.update_lyrics(
        song_id=song_id,
        lyrics=payload.lyrics,
        synced_lyrics=payload.synced_lyrics,
    )


@router.delete("/{song_id}", response_model=dict)
def delete_lyrics(song_id: UUID):
    return lyrics_service.delete_lyrics(song_id)

from uuid import UUID

from fastapi import APIRouter

from app.schemas.lyrics import (
    LyricsUpload,
    LyricsUpdate,
    LyricsResponse,
)

from app.models.lyrics import LyricsModel
from app.services.lyrics import lyrics_service

router = APIRouter()


@router.post("/upload", response_model=dict)
def upload_lyrics(payload: LyricsUpload):
    print("=== Upload reçu ===")
    print(payload)

    lyric = LyricsModel(
        song_id=payload.song_id,
        artist_id=payload.artist_id,
        title=payload.title,
        language=payload.language,
        lyrics=payload.lyrics,
        synced_lyrics=payload.synced_lyrics,
        allow_translation=payload.allow_translation,
        allow_slowed=payload.allow_slowed,
    )

    print("=== Modèle créé ===")
    print(lyric)

    return lyrics_service.upload_lyrics(lyric)



@router.get("/{song_id}", response_model=LyricsResponse)
def get_lyrics(song_id: UUID):
    return lyrics_service.get_lyrics(song_id)


@router.get("/{song_id}/synced", response_model=dict)
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
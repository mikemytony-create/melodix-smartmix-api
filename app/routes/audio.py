from uuid import UUID

from fastapi import APIRouter

from app.schemas.audio import AudioGenerateRequest
from app.services.audio import audio_service

router = APIRouter()


@router.post("/slowed")
def generate_slowed(request: AudioGenerateRequest):
    return audio_service.generate_audio(
        song_id=request.song_id,
        effect="slowed",
    )


@router.post("/speedup")
def generate_speedup(request: AudioGenerateRequest):
    return audio_service.generate_audio(
        song_id=request.song_id,
        effect="speedup",
    )


@router.post("/pitch")
def generate_pitch(request: AudioGenerateRequest):
    return audio_service.generate_audio(
        song_id=request.song_id,
        effect="pitch",
    )


@router.get("/{audio_id}")
def get_audio(audio_id: UUID):
    return audio_service.get_audio(audio_id)


@router.delete("/{audio_id}")
def delete_audio(audio_id: UUID):
    return audio_service.delete_audio(audio_id)
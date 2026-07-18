from fastapi import APIRouter
from uuid import UUID

from schemas.translation import TranslationRequest
from services.translation import translation_service

router = APIRouter()


@router.post("/translate")
def translate(request: TranslationRequest):
    return translation_service.translate(
        song_id=request.song_id,
        target_language=request.target_language,
    )

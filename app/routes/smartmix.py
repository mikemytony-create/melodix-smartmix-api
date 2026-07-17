from app.models.smartmix_request import SmartMixRequest
from fastapi import APIRouter
from app.services.smartmix_engine import SmartMixEngine

router = APIRouter(
    prefix="/smartmix",
    tags=["SmartMix"]
)

engine = SmartMixEngine()


@router.get("/health")
def health():
    return {
        "service": "SmartMix",
        "status": "healthy"
    }


@router.post("/generate")
def generate(request: SmartMixRequest):

    return engine.generate_playlist(
        mood=request.mood,
        favorite_artists=request.favorite_artists,
        favorite_genres=request.favorite_genres
    )
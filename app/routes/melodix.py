from fastapi import APIRouter
from app.models.smartmix_request import SmartMixRequest
from app.services.smartmix_engine import SmartMixEngine

router = APIRouter(
    prefix="/melodix",
    tags=["Melodix"]
)

engine = SmartMixEngine()

@router.post("/smartmix")
def smartmix(request: SmartMixRequest):
    return engine.generate_playlist(
        mood=request.mood,
        favorite_artists=request.favorite_artists,
        favorite_genres=request.favorite_genres
    )
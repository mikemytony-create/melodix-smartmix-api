from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.cloud.storage import save_song_to_cloud
import uuid

router = APIRouter()

@router.post("/upload")
async def upload_song(file: UploadFile = File(...), user_id: str = "guest"):
    """
    Upload une chanson mp3 dans le cloud et renvoie un song_id
    """
    # Vérifier que c'est bien un mp3
    if not file.filename.endswith(".mp3"):
        raise HTTPException(status_code=400, detail="Seulement les fichiers .mp3")
    
    # Générer un ID unique pour la chanson
    song_id = str(uuid.uuid4())
    
    # Sauvegarder via le service
    url = await save_song_to_cloud(file, song_id, user_id)
    
    return {
        "success": True,
        "song_id": song_id,
        "url": url,
        "message": "Chanson sauvegardée"
    }


@router.get("/mes-chansons/{user_id}")
async def get_user_songs(user_id: str):
    """
    Récupère toutes les chansons d'un user
    """
    # Pour l'instant on renvoie vide. On branchera Firebase après
    return {"user_id": user_id, "songs": []}
import os
import shutil

UPLOAD_FOLDER = "uploads"

# Créer le dossier s'il n'existe pas
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

async def save_song_to_cloud(file: UploadFile, song_id: str, user_id: str):
    file_path = f"{UPLOAD_FOLDER}/{user_id}_{song_id}.mp3"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # L'URL sera l'URL de ton API + le chemin du fichier
    url = f"/static/{user_id}_{song_id}.mp3"
    return url
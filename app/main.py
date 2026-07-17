import os
from fastapi import FastAPI
from app.routes import smartmix, lyrics, translation, audio, cloud, users, health
from fastapi.staticfiles import StaticFiles
import uvicorn

os.makedirs("uploads", exist_ok=True) # <-- MET LE ICI, LIGNE 6

app = FastAPI(title="Melodix API V1")
app.mount("/static", StaticFiles(directory="uploads"), name="static")

app.include_router(smartmix.router, prefix="/v1/smartmix", tags=["SmartMix"])
# ... le reste

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
app.include_router(smartmix.router, prefix="/v1/smartmix", tags=["SmartMix"])
app.include_router(lyrics.router, prefix="/v1/paroles", tags=["Paroles"])
app.include_router(translation.router, prefix="/v1/traduire", tags=["Traduction"])
app.include_router(audio.router, prefix="/v1/audio", tags=["Audio"])
app.include_router(cloud.router, prefix="/v1/cloud", tags=["Cloud"])
app.include_router(users.router, prefix="/v1/users", tags=["Users"])
app.include_router(health.router, prefix="/v1", tags=["Health"])
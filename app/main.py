from fastapi import FastAPI
from app.routes.smartmix import router as smartmix_router
from app.routes.melodix import router as melodix_router
app = FastAPI(
    title="Melodix SmartMix API",
    description="Official AI API for Melodix SmartMix",
    version="1.0.0"
)

app.include_router(smartmix_router)
app.include_router(melodix_router)
@app.get("/")
def home():
    return {
        "message": "Welcome to Melodix SmartMix API",
        "status": "online",
        "version": "1.0.0"
    }
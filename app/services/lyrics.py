from uuid import UUID
from typing import Optional


class LyricsService:

    def upload_lyrics(
        self,
        song_id: UUID,
        lyrics: str,
        synced_lyrics: Optional[str] = None,
    ):
        return {
            "message": "Lyrics uploaded successfully",
            "song_id": str(song_id),
            "status": "success"
        }

    def get_lyrics(self, song_id: UUID):
        return {
            "song_id": song_id,
            "lyrics": "Aucune parole enregistrée pour le moment.",
            "synced_lyrics": None,
            "language": "fr"
        }

    def get_synced_lyrics(self, song_id: UUID):
        return {
            "song_id": song_id,
            "lyrics": "Aucune parole synchronisée.",
            "synced_lyrics": None,
            "language": "fr"
        }

    def update_lyrics(
        self,
        song_id: UUID,
        lyrics: str,
        synced_lyrics: Optional[str] = None,
    ):
        return {
            "message": "Lyrics updated successfully",
            "song_id": str(song_id),
            "status": "success"
        }

    def delete_lyrics(self, song_id: UUID):
        return {
            "message": "Lyrics deleted successfully",
            "song_id": str(song_id),
            "status": "success"
        }


lyrics_service = LyricsService()

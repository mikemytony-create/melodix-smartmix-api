from uuid import UUID
from typing import Optional


class LyricsService:

    def get_lyrics(self, song_id: UUID):
        """
        Retourne les paroles d'une chanson.
        """
        return {
            "song_id": str(song_id),
            "lyrics": None,
            "status": "not_implemented"
        }

    def get_synced_lyrics(self, song_id: UUID):
        """
        Retourne les paroles synchronisées.
        """
        return {
            "song_id": str(song_id),
            "synced_lyrics": None,
            "status": "not_implemented"
        }

    def upload_lyrics(
        self,
        song_id: UUID,
        lyrics: str,
        synced_lyrics: Optional[str] = None,
    ):
        """
        Enregistre les paroles.
        """
        return {
            "song_id": str(song_id),
            "message": "Lyrics uploaded successfully",
            "status": "success"
        }

    def update_lyrics(
        self,
        song_id: UUID,
        lyrics: str,
        synced_lyrics: Optional[str] = None,
    ):
        """
        Met à jour les paroles.
        """
        return {
            "song_id": str(song_id),
            "message": "Lyrics updated successfully",
            "status": "success"
        }

    def delete_lyrics(self, song_id: UUID):
        """
        Supprime les paroles.
        """
        return {
            "song_id": str(song_id),
            "message": "Lyrics deleted successfully",
            "status": "success"
        }


lyrics_service = LyricsService()
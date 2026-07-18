from uuid import UUID
from typing import Optional

from app.models.lyrics import LyricsModel

# Base de données temporaire (sera remplacée par PostgreSQL)
lyrics_db = {}


class LyricsService:

    def upload_lyrics(
        self,
        lyric: LyricsModel,
    ):
        """
        Enregistre les paroles d'une chanson.
        """

        lyrics_db[str(lyric.song_id)] = lyric

        return {
            "status": "success",
            "message": "Lyrics uploaded successfully.",
            "song_id": str(lyric.song_id),
        }

    def get_lyrics(self, song_id: UUID):
        """
        Retourne les paroles.
        """

        lyric = lyrics_db.get(str(song_id))

        if lyric is None:
            return {
                "status": "error",
                "message": "Lyrics not found."
            }

        return lyric

    def get_synced_lyrics(self, song_id: UUID):
        """
        Retourne les paroles synchronisées.
        """

        lyric = lyrics_db.get(str(song_id))

        if lyric is None:
            return {
                "status": "error",
                "message": "Lyrics not found."
            }

        return {
            "song_id": lyric.song_id,
            "synced_lyrics": lyric.synced_lyrics,
            "status": "success"
        }

    def update_lyrics(
        self,
        song_id: UUID,
        lyrics: str,
        synced_lyrics: Optional[str] = None,
    ):

        lyric = lyrics_db.get(str(song_id))

        if lyric is None:
            return {
                "status": "error",
                "message": "Lyrics not found."
            }

        lyric.lyrics = lyrics
        lyric.synced_lyrics = synced_lyrics

        lyrics_db[str(song_id)] = lyric

        return {
            "status": "success",
            "message": "Lyrics updated successfully."
        }

    def delete_lyrics(self, song_id: UUID):

        if str(song_id) not in lyrics_db:
            return {
                "status": "error",
                "message": "Lyrics not found."
            }

        del lyrics_db[str(song_id)]

        return {
            "status": "success",
            "message": "Lyrics deleted successfully."
        }


lyrics_service = LyricsService()
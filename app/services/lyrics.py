from uuid import UUID
from typing import Dict

from app.models.lyrics import LyricsModel

# Base de données temporaire en mémoire
lyrics_db: Dict[str, LyricsModel] = {}


class LyricsService:

    def upload_lyrics(self, lyric: LyricsModel):

        lyrics_db[str(lyric.song_id)] = lyric

        return {
            "status": "success",
            "message": "Lyrics uploaded successfully",
            "song_id": str(lyric.song_id)
        }

    def get_lyrics(self, song_id: UUID):

        lyric = lyrics_db.get(str(song_id))

        if lyric is None:
            return {
                "status": "error",
                "message": "Lyrics not found"
            }

        return lyric

    def get_synced_lyrics(self, song_id: UUID):

        lyric = lyrics_db.get(str(song_id))

        if lyric is None:
            return {
                "status": "error",
                "message": "Lyrics not found"
            }

        return {
            "song_id": lyric.song_id,
            "synced_lyrics": lyric.synced_lyrics
        }

    def update_lyrics(self, song_id: UUID, lyric: LyricsModel):

        if str(song_id) not in lyrics_db:
            return {
                "status": "error",
                "message": "Lyrics not found"
            }

        lyrics_db[str(song_id)] = lyric

        return {
            "status": "success",
            "message": "Lyrics updated successfully"
        }

    def delete_lyrics(self, song_id: UUID):

        if str(song_id) not in lyrics_db:
            return {
                "status": "error",
                "message": "Lyrics not found"
            }

        del lyrics_db[str(song_id)]

        return {
            "status": "success",
            "message": "Lyrics deleted successfully"
        }


lyrics_service = LyricsService()
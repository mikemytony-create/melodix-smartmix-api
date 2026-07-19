from uuid import UUID
from datetime import datetime

from app.models.lyrics import LyricsModel

# Base de données temporaire en mémoire
lyrics_db = {}


class LyricsService:

    def upload_lyrics(self, lyric: LyricsModel):
        lyrics_db[str(lyric.song_id)] = lyric

        return {
            "status": "success",
            "message": "Lyrics uploaded successfully",
            "song_id": str(lyric.song_id),
        }

    def get_lyrics(self, song_id: UUID):
        lyric = lyrics_db.get(str(song_id))

        if lyric is None:
            return {
                "song_id": song_id,
                "lyrics": None,
                "synced_lyrics": None,
                "language": None,
            }

        return {
            "song_id": lyric.song_id,
            "lyrics": lyric.lyrics,
            "synced_lyrics": lyric.synced_lyrics,
            "language": lyric.language,
        }

    def get_synced_lyrics(self, song_id: UUID):
        lyric = lyrics_db.get(str(song_id))

        if lyric is None:
            return {
                "status": "error",
                "message": "Lyrics not found",
            }

        return {
            "song_id": str(lyric.song_id),
            "synced_lyrics": lyric.synced_lyrics,
        }

    def update_lyrics(self, song_id: UUID, lyrics: str, synced_lyrics: str = None):
        lyric = lyrics_db.get(str(song_id))

        if lyric is None:
            return {
                "status": "error",
                "message": "Lyrics not found",
            }

        lyric.lyrics = lyrics
        lyric.synced_lyrics = synced_lyrics
        lyric.updated_at = datetime.utcnow()

        lyrics_db[str(song_id)] = lyric

        return {
            "status": "success",
            "message": "Lyrics updated successfully",
        }

    def delete_lyrics(self, song_id: UUID):
        if str(song_id) not in lyrics_db:
            return {
                "status": "error",
                "message": "Lyrics not found",
            }

        del lyrics_db[str(song_id)]

        return {
            "status": "success",
            "message": "Lyrics deleted successfully",
        }


lyrics_service = LyricsService()
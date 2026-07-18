from uuid import UUID
from typing import Optional

from models.lyrics import LyricsModel

# Base de données temporaire
lyrics_db = {}


class LyricsService:

    def upload_lyrics(
        self,
        song_id: UUID,
        lyrics: str,
        synced_lyrics: Optional[str] = None,
    ):

        lyric = LyricsModel(
            song_id=song_id,
            artist_id=UUID("00000000-0000-0000-0000-000000000001"),
            title="Unknown",
            language="fr",
            lyrics=lyrics,
            synced_lyrics=synced_lyrics,
        )

        lyrics_db[str(song_id)] = lyric

        return {
            "message": "Lyrics uploaded successfully",
            "song_id": str(song_id),
            "status": "success"
        }

    def get_lyrics(self, song_id: UUID):

        lyric = lyrics_db.get(str(song_id))

        if lyric:
            return lyric

        return {
            "song_id": song_id,
            "lyrics": None,
            "synced_lyrics": None,
            "language": None
        }

    def get_synced_lyrics(self, song_id: UUID):

        lyric = lyrics_db.get(str(song_id))

        if lyric:
            return {
                "song_id": lyric.song_id,
                "lyrics": lyric.lyrics,
                "synced_lyrics": lyric.synced_lyrics,
                "language": lyric.language,
            }

        return {
            "song_id": song_id,
            "lyrics": None,
            "synced_lyrics": None,
            "language": None,
        }

    def update_lyrics(
        self,
        song_id: UUID,
        lyrics: str,
        synced_lyrics: Optional[str] = None,
    ):

        lyric = lyrics_db.get(str(song_id))

        if lyric:
            lyric.lyrics = lyrics
            lyric.synced_lyrics = synced_lyrics

        return {
            "message": "Lyrics updated successfully",
            "song_id": str(song_id),
            "status": "success"
        }

    def delete_lyrics(self, song_id: UUID):

        lyrics_db.pop(str(song_id), None)

        return {
            "message": "Lyrics deleted successfully",
            "song_id": str(song_id),
            "status": "success"
        }


lyrics_service = LyricsService()

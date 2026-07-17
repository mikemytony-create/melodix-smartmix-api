from services.music_database import SONGS
from services.smartmix_config import *
from services.ai_engine import AIEngine
from models.user_profile import UserProfile

class SmartMixEngine:

    def __init__(self):
        self.ai = AIEngine()
        
    def generate_playlist(
        self,
        mood: str,
        favorite_artists: list,
        favorite_genres: list
    ):
        playlist = []

        for song in SONGS:
            profile = UserProfile(
                favorite_artists=favorite_artists,
                favorite_genres=favorite_genres,
                liked_songs=[],
                skipped_songs=[],
                recently_played=[]
            )
            score = 0

            # Humeur
            if mood.lower() in [m.lower() for m in song.mood]:
                score += MOOD_WEIGHT

            # Artiste préféré
            if song.artist.lower() in [a.lower() for a in favorite_artists]:
                score += ARTIST_WEIGHT

            # Genre préféré
            if song.genre.lower() in [g.lower() for g in favorite_genres]:
                score += GENRE_WEIGHT

            if score > 0:
                score += self.ai.calculate_ai_score(profile, song)
                playlist.append({
                    "id": song.id,
                    "title": song.title,
                    "artist": song.artist,
                    "genre": song.genre,
                    "score": score
                })

        playlist.sort(key=lambda x: x["score"], reverse=True)

        return {
            "mood": mood,
            "playlist": playlist
        }
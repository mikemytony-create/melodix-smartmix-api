from app.services.music_database import SONGS
from app.services.smartmix_config import CONFIG
from app.services.ai_engine import AIEngine
from app.models.user_profile import UserProfile


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

            # Correspondance de l'humeur
            if mood.lower() in [m.lower() for m in song.mood]:
                score += CONFIG["MOOD_WEIGHT"]

            # Artiste préféré
            if song.artist.lower() in [a.lower() for a in favorite_artists]:
                score += CONFIG["ARTIST_WEIGHT"]

            # Genre préféré
            if song.genre.lower() in [g.lower() for g in favorite_genres]:
                score += CONFIG["GENRE_WEIGHT"]

            # Score IA
            score += self.ai.calculate_ai_score(profile, song)

            if score > 0:
                playlist.append({
                    "id": song.id,
                    "title": song.title,
                    "artist": song.artist,
                    "genre": song.genre,
                    "score": score
                })

        playlist.sort(
            key=lambda music: music["score"],
            reverse=True
        )

        max_songs = CONFIG.get("MAX_SONGS_PER_MIX", 20)

        return {
            "mood": mood,
            "total": min(len(playlist), max_songs),
            "playlist": playlist[:max_songs]
        }


smartmix_engine = SmartMixEngine()
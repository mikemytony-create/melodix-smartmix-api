from app.models.user_profile import UserProfile
from app.services.music_database import SONGS


class RecommendationEngine:

    def update_profile(
        self,
        profile: UserProfile,
        song_id: int,
        liked: bool
    ):

        if liked:
            if song_id not in profile.liked_songs:
                profile.liked_songs.append(song_id)
        else:
            if song_id not in profile.skipped_songs:
                profile.skipped_songs.append(song_id)

        if song_id not in profile.recently_played:
            profile.recently_played.append(song_id)

        return profile

    def recommend(
        self,
        profile: UserProfile,
        mood: str = None,
        limit: int = 20
    ):

        recommendations = []

        for song in SONGS:

            score = 0

            # Humeur
            if mood and mood.lower() in [m.lower() for m in song.mood]:
                score += 50

            # Artiste préféré
            if song.artist.lower() in [
                artist.lower()
                for artist in profile.favorite_artists
            ]:
                score += 30

            # Genre préféré
            if song.genre.lower() in [
                genre.lower()
                for genre in profile.favorite_genres
            ]:
                score += 20

            # Déjà likée
            if song.id in profile.liked_songs:
                score += 40

            # Ignorée
            if song.id in profile.skipped_songs:
                score -= 30

            # Jamais écoutée
            if song.id not in profile.recently_played:
                score += 10

            # Artiste indépendant
            if getattr(song, "is_independent", False):
                score += 35

            # Artiste local
            if getattr(song, "is_local", False):
                score += 15

            recommendations.append({
                "song": song,
                "score": score
            })

        recommendations.sort(
            key=lambda item: item["score"],
            reverse=True
        )

        playlist = []
        artists = set()

        for item in recommendations:

            song = item["song"]

            if song.artist in artists:
                continue

            artists.add(song.artist)
            playlist.append(song)

            if len(playlist) >= limit:
                break

        return playlist


recommendation_engine = RecommendationEngine()
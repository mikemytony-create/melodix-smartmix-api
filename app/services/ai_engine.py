
from app.models.user_profile import UserProfile
from app.models.user_profile import UserProfile


class AIEngine:

    def calculate_ai_score(
        self,
        profile: UserProfile,
        song
    ):

        score = 0

        # Genres favoris
        if song.genre in profile.favorite_genres:
            score += 25

        # Artistes favoris
        if song.artist in profile.favorite_artists:
            score += 30

        # Chanson aimée
        if song.id in profile.liked_songs:
            score += 35

        # Chanson ignorée
        if song.id in profile.skipped_songs:
            score -= 50

        return score
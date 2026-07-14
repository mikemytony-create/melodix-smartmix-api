from app.models.user_profile import UserProfile

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
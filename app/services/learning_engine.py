from app.models.user_profile import UserProfile

class LearningEngine:

    def learn(self, profile: UserProfile, song_id: int, listened_percent: int):

        if listened_percent >= 80:
            if song_id not in profile.liked_songs:
                profile.liked_songs.append(song_id)

        elif listened_percent <= 20:
            if song_id not in profile.skipped_songs:
                profile.skipped_songs.append(song_id)

        return profile
from app.models.user_profile import UserProfile


class LearningEngine:

    def learn(
        self,
        profile: UserProfile,
        song_id: int,
        listened_percent: int
    ):

        # L'utilisateur écoute presque toute la chanson
        if listened_percent >= 80:
            if song_id not in profile.liked_songs:
                profile.liked_songs.append(song_id)

            # Si la chanson avait été ignorée auparavant
            if song_id in profile.skipped_songs:
                profile.skipped_songs.remove(song_id)

        # L'utilisateur passe rapidement la chanson
        elif listened_percent <= 20:
            if song_id not in profile.skipped_songs:
                profile.skipped_songs.append(song_id)

            # Si elle était auparavant likée
            if song_id in profile.liked_songs:
                profile.liked_songs.remove(song_id)

        # Historique de lecture
        if song_id not in profile.recently_played:
            profile.recently_played.append(song_id)

        return profile


learning_engine = LearningEngine()
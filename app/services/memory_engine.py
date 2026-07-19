from app.models.user_profile import UserProfile


class MemoryEngine:

    def remember_song(self, profile: UserProfile, song_id: int):

        if song_id not in profile.recently_played:
            profile.recently_played.append(song_id)

        return profile

    def remember_artist(self, profile: UserProfile, artist: str):

        if artist not in profile.favorite_artists:
            profile.favorite_artists.append(artist)

        return profile

    def remember_genre(self, profile: UserProfile, genre: str):

        if genre not in profile.favorite_genres:
            profile.favorite_genres.append(genre)

        return profile

    def remember_session(
        self,
        profile: UserProfile,
        song_id: int,
        artist: str,
        genre: str
    ):

        profile = self.remember_song(profile, song_id)
        profile = self.remember_artist(profile, artist)
        profile = self.remember_genre(profile, genre)

        return profile

    def clear_recent_history(self, profile: UserProfile):

        profile.recently_played.clear()

        return profile


memory_engine = MemoryEngine()
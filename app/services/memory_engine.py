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
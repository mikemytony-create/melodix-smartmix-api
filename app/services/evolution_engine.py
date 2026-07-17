from app.models.user_profile import UserProfile


class EvolutionEngine:

    def update_preferences(self, profile: UserProfile):

        artist_stats = {}
        genre_stats = {}

        for artist in profile.favorite_artists:
            artist_stats[artist] = artist_stats.get(artist, 0) + 1

        for genre in profile.favorite_genres:
            genre_stats[genre] = genre_stats.get(genre, 0) + 1

        top_artists = sorted(
            artist_stats.items(),
            key=lambda item: item[1],
            reverse=True
        )

        top_genres = sorted(
            genre_stats.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return {
            "favorite_artists": top_artists,
            "favorite_genres": top_genres
        }
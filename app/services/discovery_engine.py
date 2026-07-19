from typing import List


class DiscoveryEngine:

    def discover_similar_artists(
        self,
        favorite_artists: List[str]
    ) -> List[str]:

        similar = {

            "The Weeknd": [
                "Post Malone",
                "Bruno Mars",
                "Justin Bieber"
            ],

            "Rema": [
                "Ayra Starr",
                "Asake",
                "Omah Lay"
            ],

            "Burna Boy": [
                "Ruger",
                "Fireboy DML",
                "Wizkid"
            ],

            "Drake": [
                "Future",
                "Travis Scott",
                "21 Savage"
            ]

        }

        recommendations = []

        for artist in favorite_artists:

            if artist in similar:
                recommendations.extend(similar[artist])

        return list(set(recommendations))

    def discover_similar_genres(
        self,
        favorite_genres: List[str]
    ) -> List[str]:

        similar = {

            "Afrobeats": [
                "Afropop",
                "Amapiano",
                "Dancehall"
            ],

            "Hip-Hop": [
                "Trap",
                "Rap",
                "R&B"
            ],

            "Electronic": [
                "House",
                "Techno",
                "Synthwave"
            ],

            "Pop": [
                "Dance Pop",
                "Indie Pop",
                "Electropop"
            ]

        }

        recommendations = []

        for genre in favorite_genres:

            if genre in similar:
                recommendations.extend(similar[genre])

        return list(set(recommendations))

    def discover_new_moods(
        self,
        current_mood: str
    ) -> List[str]:

        moods = {

            "happy": [
                "party",
                "energetic",
                "dance"
            ],

            "sad": [
                "calm",
                "relax",
                "hope"
            ],

            "chill": [
                "focus",
                "dreamy",
                "romantic"
            ],

            "motivation": [
                "workout",
                "power",
                "success"
            ]

        }

        return moods.get(current_mood.lower(), [])


discovery_engine = DiscoveryEngine()
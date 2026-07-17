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

                recommendations.extend(
                    similar[artist]
                )

        return list(
            set(recommendations)
        )
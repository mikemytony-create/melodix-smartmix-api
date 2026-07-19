class ExplanationEngine:

    def explain(
        self,
        mood: str,
        artist: str,
        genre: str,
        score: int
    ):

        reasons = []

        if score >= 90:
            reasons.append("Correspond parfaitement à tes goûts.")

        elif score >= 70:
            reasons.append("Très proche de tes habitudes d'écoute.")

        elif score >= 50:
            reasons.append("Bonne recommandation selon tes préférences.")

        else:
            reasons.append("Découverte recommandée pour élargir tes goûts.")

        reasons.append(f"Humeur : {mood}")
        reasons.append(f"Artiste : {artist}")
        reasons.append(f"Genre : {genre}")
        reasons.append(f"Score SmartMix : {score}/100")

        return {
            "score": score,
            "reason": " | ".join(reasons)
        }

    def explain_playlist(self, playlist):

        explanations = []

        for song in playlist:

            explanations.append({
                "song_id": getattr(song, "id", None),
                "title": getattr(song, "title", ""),
                "artist": getattr(song, "artist", ""),
                "genre": getattr(song, "genre", ""),
                "message": "Cette chanson a été sélectionnée par SmartMix selon ton profil musical."
            })

        return explanations


explanation_engine = ExplanationEngine()
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

        else:
            reasons.append("Découverte recommandée pour élargir tes goûts.")

        reasons.append(f"Humeur : {mood}")
        reasons.append(f"Artiste : {artist}")
        reasons.append(f"Genre : {genre}")

        return {
            "score": score,
            "reason": " | ".join(reasons)
        }
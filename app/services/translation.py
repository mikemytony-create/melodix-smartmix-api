from uuid import UUID

from models.translation import TranslationModel
from services.lyrics import lyrics_db

# Base de données temporaire des traductions
translations_db = {}


class TranslationService:

    def translate(self, song_id: UUID, target_language: str):

        # 1. Vérifier que les paroles existent
        lyric = lyrics_db.get(str(song_id))

        if not lyric:
            return {
                "status": "error",
                "message": "Lyrics not found."
            }

        # 2. Vérifier les droits de traduction
        if not lyric.allow_translation:
            return {
                "status": "error",
                "message": "Translation not allowed by artist."
            }

        # 3. Vérifier si la traduction existe déjà
        cache_key = f"{song_id}_{target_language}"

        if cache_key in translations_db:
            return translations_db[cache_key]

        # 4. Traduction simulée (à remplacer plus tard)
        translated_text = f"[{target_language}] {lyric.lyrics}"

        translation = TranslationModel(
            song_id=song_id,
            source_language=lyric.language,
            target_language=target_language,
            translated_lyrics=translated_text,
            provider="mock"
        )

        # 5. Sauvegarder la traduction
        translations_db[cache_key] = translation

        return translation


translation_service = TranslationService()

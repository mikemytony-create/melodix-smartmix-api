from uuid import UUID

from app.models.translation import TranslationModel
from app.services.lyrics import lyrics_db
from app.providers.factory import TranslationFactory

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

        # 2. Vérifier que l'artiste autorise la traduction
        if not lyric.allow_translation:
            return {
                "status": "error",
                "message": "Translation not allowed by artist."
            }

        # 3. Vérifier si la traduction existe déjà
        cache_key = f"{song_id}_{target_language}"

        if cache_key in translations_db:
            return translations_db[cache_key]

        # 4. Récupérer le fournisseur de traduction
        provider = TranslationFactory.get_provider()

        # 5. Traduire les paroles
        translated_text = provider.translate(
            text=lyric.lyrics,
            source_language=lyric.language,
            target_language=target_language,
        )

        # 6. Créer le modèle de traduction
        translation = TranslationModel(
            song_id=song_id,
            source_language=lyric.language,
            target_language=target_language,
            translated_lyrics=translated_text,
            provider=provider.name,
        )

        # 7. Sauvegarder la traduction
        translations_db[cache_key] = translation

        # 8. Retourner la traduction
        return translation


translation_service = TranslationService()
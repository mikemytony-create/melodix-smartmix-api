from providers.base import TranslationProvider


class MockTranslationProvider(TranslationProvider):

    def translate(
        self,
        text: str,
        source_language: str,
        target_language: str,
    ) -> str:

        return f"[{target_language}] {text}"

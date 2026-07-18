from providers.mock import MockTranslationProvider


class TranslationFactory:

    @staticmethod
    def get_provider(name: str = "mock"):

        if name == "mock":
            return MockTranslationProvider()

        raise ValueError(f"Unknown provider: {name}")
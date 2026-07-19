from uuid import UUID

from app.models.audio import AudioModel

# Base de données temporaire en mémoire
audio_db = {}


class AudioService:

    def generate_audio(self, song_id: UUID, effect: str):

        audio = AudioModel(
            song_id=song_id,
            effect=effect,
            original_url=f"/static/audio/{song_id}.mp3",
            generated_url=f"/static/audio/{effect}_{song_id}.mp3",
        )

        audio_db[str(audio.audio_id)] = audio

        return audio

    def get_audio(self, audio_id: UUID):

        audio = audio_db.get(str(audio_id))

        if audio is None:
            return {
                "status": "error",
                "message": "Audio not found"
            }

        return audio

    def delete_audio(self, audio_id: UUID):

        if str(audio_id) not in audio_db:
            return {
                "status": "error",
                "message": "Audio not found"
            }

        del audio_db[str(audio_id)]

        return {
            "status": "success",
            "message": "Audio deleted successfully"
        }


audio_service = AudioService()
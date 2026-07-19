from uuid import UUID

from app.models.cloud import CloudFileModel

# Base de données temporaire
cloud_db = {}


class CloudService:

    def upload_song(
        self,
        song_id: UUID,
        artist_id: UUID,
        filename: str,
        file_type: str,
        file_size: int,
    ):

        cloud_file = CloudFileModel(
            song_id=song_id,
            artist_id=artist_id,
            filename=filename,
            file_type=file_type,
            file_url=f"/static/uploads/{filename}",
            file_size=file_size,
        )

        cloud_db[str(cloud_file.file_id)] = cloud_file

        return cloud_file

    def get_file(self, file_id: UUID):

        return cloud_db.get(str(file_id))

    def delete_file(self, file_id: UUID):

        if str(file_id) not in cloud_db:
            return {
                "status": "error",
                "message": "File not found"
            }

        del cloud_db[str(file_id)]

        return {
            "status": "success",
            "message": "File deleted successfully"
        }


cloud_service = CloudService()
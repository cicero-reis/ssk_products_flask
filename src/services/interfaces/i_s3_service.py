from abc import ABC, abstractmethod
from typing import Any


class IS3Service(ABC):
    @abstractmethod
    def upload_to_s3(self, file_obj: Any, stored_filename: Any) -> Any:
        """Uploads a file object to S3 with the specified stored filename."""
        pass

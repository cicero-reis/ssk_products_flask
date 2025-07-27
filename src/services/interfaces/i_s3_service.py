from typing import Any
from abc import ABC, abstractmethod

class IS3Service(ABC):
    @abstractmethod
    def upload_to_s3(self, file_obj: Any, stored_filename: Any) -> Any:
        """Uploads a file object to S3 with the specified stored filename."""
        pass
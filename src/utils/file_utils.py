import os
import re
import uuid
from typing import Any


def generate_stored_filename(original_name: Any) -> Any:
    ext = os.path.splitext(original_name)[1].lower()

    safe_name = re.sub(r"[^a-zA-Z0-9_-]", "", os.path.splitext(original_name)[0])

    unique_id = uuid.uuid4().hex

    return f"{safe_name}_{unique_id}{ext}"

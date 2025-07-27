import os
from typing import Any
import boto3
from src.services.interfaces.i_s3_service import IS3Service
from botocore.exceptions import BotoCoreError, NoCredentialsError

class S3Service(IS3Service):

    def __init__(self) -> Any:
        self.s3_client = boto3.client(
            "s3",
            region_name=os.environ.get("AWS_REGION", "us-east-1"),
            aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID", "test"),  # nosec B105
            aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY", "test"),  # nosec B105
            endpoint_url=os.environ.get("AWS_ENDPOINT_URL", "http://localstack:4566"),
            config=boto3.session.Config(s3={"addressing_style": "path"})  # 💡 caminho correto para force_path_style
        )
        self.bucket_name = os.environ.get("S3_BUCKET_NAME", "sskbucket")

    def upload_to_s3(self, file_obj: Any, stored_filename: Any) -> Any:
        try:
            self.s3_client.upload_fileobj(
                Fileobj=file_obj, Bucket=self.bucket_name, Key=stored_filename, ExtraArgs={"ACL": "public-read"}
            )
        except (BotoCoreError, NoCredentialsError) as e:
            raise RuntimeError(f"Failed to upload file to S3: {str(e)}")

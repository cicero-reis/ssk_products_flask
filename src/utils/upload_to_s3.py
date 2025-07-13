from typing import Any
import boto3

s3_client = boto3.client(
    "s3",
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    endpoint_url="http://localstack:4566",  # Para uso com LocalStack
)

BUCKET_NAME = "sskproduct"


def upload_to_s3(file_obj: Any, stored_filename: Any) -> Any:
    s3_client.upload_fileobj(
        Fileobj=file_obj, Bucket=BUCKET_NAME, Key=stored_filename, ExtraArgs={"ACL": "public-read"}
    )

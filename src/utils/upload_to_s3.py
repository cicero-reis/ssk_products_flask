from typing import Any
import os

import boto3

# Obter credenciais das variáveis de ambiente ou usar valores padrão para LocalStack
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY_ID", "test_key")  # nosec B105
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "test_secret")  # nosec B105
ENDPOINT_URL = os.environ.get("AWS_ENDPOINT_URL", "http://localstack:4566")

s3_client = boto3.client(
    "s3",
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    endpoint_url=ENDPOINT_URL,  # Para uso com LocalStack
)

BUCKET_NAME = os.environ.get("S3_BUCKET_NAME", "sskproduct")


def upload_to_s3(file_obj: Any, stored_filename: Any) -> Any:
    s3_client.upload_fileobj(
        Fileobj=file_obj, Bucket=BUCKET_NAME, Key=stored_filename, ExtraArgs={"ACL": "public-read"}
    )

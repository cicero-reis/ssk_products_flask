provider "aws" {
  region                      = var.region
  access_key                  = var.access_key
  secret_key                  = var.secret_key
  s3_use_path_style           = true
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    sqs        = var.localstack
    s3         = var.localstack
    cloudwatch = var.localstack
    logs       = var.localstack
  }

  default_tags {
    tags = local.common_tags
  }
}

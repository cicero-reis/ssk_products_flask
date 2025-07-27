terraform {
  required_version = "1.12.2"

  required_providers {
    aws = {
      version = "4.29.0"
      source  = "hashicorp/aws"
    }
  }
}

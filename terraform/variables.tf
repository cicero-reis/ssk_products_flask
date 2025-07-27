variable "region" {
  description = "Indicates the AWS Region"
  type        = string
  default     = "us-east-1"
}

variable "localstack" {
  description = "Endpoint localstack"
  type        = string
  default     = "http://localhost:4566"
}

variable "access_key" {
  description = "AWS access_key"
  type        = string
  default     = "test"
}

variable "secret_key" {
  description = "AWS secret_key"
  type        = string
  default     = "test"
}

variable "s3_buckets" {
  description = "Lista de buckets S3 e suas configurações"
  type = map(object({
    versioning_enabled = bool
    force_destroy      = bool
  }))
}

variable "ssk_queue" {
  description = "SSK Queue"
  type        = string
  default     = "ssk_queue"
}

variable "ssk_queue_dlq" {
  description = "SSK Queue DLQ"
  type        = string
  default     = "ssk_dlq"
}

variable "cloudwatch_log_group_name" {
  description = "Nome do CloudWatch Log Group"
  type        = string
  default     = "laravel-queue-producer-group"
}

variable "cloudwatch_log_stream_name" {
  description = "Nome do CloudWatch Log Stream"
  type        = string
  default     = "laravel-queue-producer-stream"
}

variable "tags" {
  description = "Tags to set..."
  type        = map(string)
  default     = {}
}


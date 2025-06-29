resource "aws_cloudwatch_log_group" "ssk_log_group" {
  name              = var.cloudwatch_log_group_name
  retention_in_days = 7
  tags              = var.tags
}

resource "aws_cloudwatch_log_stream" "laravel_log_stream" {
  name           = var.cloudwatch_log_stream_name
  log_group_name = aws_cloudwatch_log_group.ssk_log_group.name
}

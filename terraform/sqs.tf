resource "aws_sqs_queue" "ssk_queue" {
  name                       = var.ssk_queue
  delay_seconds              = 10
  max_message_size           = 2048
  message_retention_seconds  = 131072
  visibility_timeout_seconds = 60
  receive_wait_time_seconds  = 20
  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.ssk_queue_dlq.arn
    maxReceiveCount     = 4
  })
  tags = var.tags
}

resource "aws_sqs_queue" "ssk_queue_dlq" {
  name = var.ssk_queue_dlq
}

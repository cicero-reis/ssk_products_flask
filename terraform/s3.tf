resource "aws_s3_bucket_policy" "public_folder_policy" {
  for_each = var.s3_buckets

  bucket = aws_s3_bucket.buckets[each.key].id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "AllowReadOnlyAccessToPublicFolder"
        Effect    = "Allow"
        Principal = "*"
        Action    = "s3:GetObject"
        Resource  = "${aws_s3_bucket.buckets[each.key].arn}/public/*"
      }
    ]
  })
}


resource "aws_s3_bucket" "buckets" {
  for_each = var.s3_buckets

  bucket        = each.key
  force_destroy = each.value.force_destroy
  tags          = var.tags
}

resource "aws_s3_bucket_versioning" "versioning" {
  for_each = var.s3_buckets

  bucket = aws_s3_bucket.buckets[each.key].id

  versioning_configuration {
    status = each.value.versioning_enabled ? "Enabled" : "Suspended"
  }
}

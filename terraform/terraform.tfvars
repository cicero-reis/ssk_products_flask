s3_buckets = {
  "ssk_bucket" = {
    versioning_enabled = true
    force_destroy      = false
  }
}

tags = {
  Environment = "dev"
  Project     = "ssk"
}



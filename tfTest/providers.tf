terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "= 3.68.0"
    }
  }
}

provider "aws" {
  # explicit default provider
  region = "us-west-2"
}

resource "aws_secretsmanager_secret" "test_secret" {
  name_prefix = "dweintraub_test_secret"
  description = "testing secret replication"
  
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "= 4.6.0"
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

  #replica {
  #  region = "us-east-2"
  #} 
  
}

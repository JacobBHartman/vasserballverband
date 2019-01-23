/*
 * ???/vasserballverband/terraform/variables.tf
 * This file contains variables for a Terraform project.
 * Variables are sorted alphabetically.
 */

variable "ami" {
  description = "Amazon Linux AMI"
  default     = "ami-4fffc834"
}

variable "aws_region" {
  description = "Region for the system. Author is from the US"
  default     = "us-east-1"
}

variable "bootstrap_path" {
  description = "Script to install Docker Engine"
  default     = "install-docker.sh"
}

variable "credentials-localToAws" {
  description = "Credentials for local to AWS"
  default     = "~/vasserballverband/terraform/credentials-localToAws"
}

variable "instance_type" {
  description = "Type of AWS instance"
  default     = "t2.micro"
}

variable "key_path" {
  description = "SSH Public Key path"
  default     = "/home/jbhartman99/.ssh/id_rsa.pub"
}



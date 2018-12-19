# */vasserballverband/terraform/main.tf
provider "aws" {
  access_key = "${var.aws_access_key}"
  secret_key = "${var.aws_secret_key}"
  region     = "${var.region}"
}

resource "aws_vpc" "vpc_name" {
  cidr_block           = "59.0.0.0/16"
  instance_tenancy     = "default"
  enable_dns_support   = "true"
  enable_dns_hostnames = "false"
}

resource "aws_subnet" "subnet_public_name" {
  vpc_id            = "${aws_vpc.vpc_name.id}"
  cidr_block        = "59.0.2.0/24"
  availability_zone = "us-east-1e"
}

resource "aws_subnet" "subnet_private_name" {
  vpc_id            = "${aws_vpc.vpc_name.id}"
  cidr_block        = "59.0.3.0/24"
  availability_zone = "us-east-1f"
}

resource "aws_route_table" "route_table_name" {
  vpc_id = "${aws_vpc.vpc_name.id}"
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = "${aws_internet_gateway.gateway_name.id}"
  }
}

resource "aws_internet_gateway" "gateway_name" {
  vpc_id = "${aws_vpc.vpc_name.id}"
}

resource "aws_route_table_association" "rt_assoc" {
  subnet_id      = "${aws_subnet.subnet_private_name.id}"
  route_table_id = "${aws_route_table.route_table_name.id}"
}

resource "aws_security_group" "security_public" {
  name        = "security_public"
  description = "Allow all inbound traffic"
  vpc_id      = "${aws_vpc.vpc_name.id}"

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "security_private" {
  name        = "security_private"
  description = "Allow some traffic"
  vpc_id      = "${aws_vpc.vpc_name.id}"
  
  # ingress...
  # redis
  # postgres
  # mysql
  # etc.

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["59.0.2.0/24"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
}


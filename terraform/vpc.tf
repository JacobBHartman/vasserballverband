/*
 * file:        ?/vasserballverband/terraform/vpc.tf
 * description: This terraform file describes a basic VPC
 *              in AWS with one private subnet and one 
 *              public subnet. It includes everything one needs
 *              to build a basic VPC in AWS including an internet
 *              gateway, route table
 *              VPC --- subnet_private
 *                   |- subnet_public
 *
 */
resource "aws_vpc" "main" {
  cidr_block           = "${var.cidr_vpc}"
  instance_tenancy     = "default"
  enable_dns_support   = "true"
  enable_dns_hostnames = "false"
}

resource "aws_subnet" "public" {
  vpc_id            = "${aws_vpc.main.id}"
  cidr_block        = "${var.cidr_subnet_public}"
  availability_zone = "us-east-1e"
}

resource "aws_subnet" "private" {
  vpc_id            = "${aws_vpc.main.id}"
  cidr_block        = "${var.cidr_subnet_private}"
  availability_zone = "us-east-1f"
}

resource "aws_internet_gateway" "public" {
  vpc_id = "${aws_vpc.main.id}"
}

resource "aws_route_table" "public" {
  vpc_id = "${aws_vpc.main.id}"
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = "${aws_internet_gateway.public.id}"
  }
}

resource "aws_route_table_association" "public" {
  subnet_id      = "${aws_subnet.public.id}"
  route_table_id = "${aws_route_table.public.id}"
}

resource "aws_security_group" "public" {
  name        = "security_public"
  description = "Allow all inbound traffic"
  vpc_id      = "${aws_vpc.main.id}"

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

resource "aws_security_group" "private" {
  name        = "security_private"
  description = "Allow traffic from public subnet"
  vpc_id      = "${aws_vpc.main.id}"

  # ingress...
  # redis
  # postgres
  # mysql
  # etc.

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["${var.cidr_subnet_public}"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["${var.cidr_subnet_public}"]
  }
}

# */vasserballverband/terraform/main.tf
provider "aws" {
  profile                 = "terraform"
  shared_credentials_file = "${var.credentials-localToAws}"
  region                  = "${var.aws_region}"
}

resource "aws_key_pair" "main" {
  key_name   = "vbvb_local2aws"
  public_key = "${file(var.key_path)}"
}

resource "aws_security_group" "default" {
  name = "security_group"
  description = "Allow in traffic"

  ingress {
    from_port = 0
    to_port   = 65535
    protocol  = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port = 0
    to_port   = 65535
    protocol  = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port = -1
    to_port   = -1
    protocol  = "icmp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


resource "aws_instance" "worker1" {
  ami = "${var.ami}"
  instance_type = "${var.instance_type}"
  key_name      = "${aws_key_pair.main.id}"
  user_data     = "${file("${var.bootstrap_path}")}"

  vpc_security_group_ids = ["${aws_security_group.default.id}"]
  tags {
    Name = "worker1"
  }
}


resource "aws_instance" "master0" {
  ami = "${var.ami}"
  instance_type = "${var.instance_type}"
  key_name      = "${aws_key_pair.main.id}"
  user_data     = "${file("${var.bootstrap_path}")}"

  vpc_security_group_ids = ["${aws_security_group.default.id}"]
  tags {
    Name = "master0"
  }
}


resource "aws_instance" "master1" {
  ami = "${var.ami}"
  instance_type = "${var.instance_type}"
  key_name      = "${aws_key_pair.main.id}"
  user_data     = "${file("${var.bootstrap_path}")}"

  vpc_security_group_ids = ["${aws_security_group.default.id}"]
  tags {
    Name = "master1"
  }
}


resource "aws_instance" "master2" {
  ami = "${var.ami}"
  instance_type = "${var.instance_type}"
  key_name      = "${aws_key_pair.main.id}"
  user_data     = "${file("${var.bootstrap_path}")}"

  vpc_security_group_ids = ["${aws_security_group.default.id}"]
  tags {
    Name = "master2"
  }
}


resource "aws_instance" "worker0" {
  ami = "${var.ami}"
  instance_type = "${var.instance_type}"
  key_name      = "${aws_key_pair.main.id}"
  user_data     = "${file("${var.bootstrap_path}")}"

  vpc_security_group_ids = ["${aws_security_group.default.id}"]
  tags {
    Name = "worker0"
  }
}

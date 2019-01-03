# */vasserballverband/terraform/main.tf
provider "aws" {
  profile                 = "terraform"
  shared_credentials_file = "${var.credentials-localToAws"
  region                  = "${var.aws_region}"
}

resource "aws_key_pair" "main" {
  key_name   = "vpc_test"
  public_key = "${file('${var.key_path}')}"
}

resource "aws_instance" "webdev" {
  ami           = "${var.ami}"
  instance_type = "t1.micro"
  key_name      = "${aws_key_pair.main.id}"
  subnet_id     = "${aws_subnet.public.id}"
  user_data     = "${file('install.sh')}"

  vpc_security_group_ids      = ["${aws_security_group.public.id}"]
  associate_public_ip_address = true
  source_dest_check           = false
}

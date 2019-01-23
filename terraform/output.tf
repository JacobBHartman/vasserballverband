output "master0-ip" {
  value = "${aws_instance.master0.public_ip}"
}

output "master1-ip" {
  value = "${aws_instance.master1.public_ip}"
}

output "master2-ip" {
  value = "${aws_instance.master2.public_ip}"
}

output "worker0-ip" {
  value = "${aws_instance.worker0.public_ip}"
}

output "worker1-ip" {
  value = "${aws_instance.worker1.public_ip}"
}

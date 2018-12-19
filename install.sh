#!/bin/bash
# */vasserballverband/vbvb/install.sh

# Update and upgrade
sudo apt update && sudo apt upgrade -y

# Python 3.6.7 is pre-installed on Ubuntu 18.04 so just install pip3 and tree
sudo apt install -y python3-pip tree

# Install all Django dependencies
sudo -H pip3 install django djangorestframework django_extensions

# Install Terraform
# We need wget and it's already installed
sudo apt install unzip
wget https://releases.hashicorp.com/terraform/0.11.11/terraform_0.11.11_linux_amd64.zip
unzip terra*
sudo mv terraform /usr/local/bin
terraform version
rm -f terra*

# Install Docker for Jenkins
sudo apt install -y\
	apt-transport-https \
	ca-certificates \
	curl \
	software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt update
sudo apt install -y docker-ce

# Spin up a container so we may install Jenkins
sudo docker run \
  --name "jenkins_container" \
  -u root \
  --rm \
  -d \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins-data:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkinsci/blueocean \

# Container needs to complete installation before we access it
echo "SLEEEPING FOR THE DOCKER CONTAINER DASFSFASADFASFASFDSAFDSFAF"
sleep 5s
JENKINS_ADMIN_PASSWORD=$(sudo docker exec -ti jenkins_container cat '/var/jenkins_home/secrets/initialAdminPassword')

echo "All installations attempted"

# Cleanup
sudo apt autoremove -y

# We now want to
# change ALLOWED_HOSTS in */vasserballverband/vbvb/vbvb/settings.py to your instance's
# public IP. To get the public IP we have to use
EXTERNAL_IP=$(curl -H "Metadata-Flavor: Google" http://169.254.169.254/computeMetadata/v1/instance/network-interfaces/0/access-configs/0/external-ip)
# because GCP's virtualization of hardware leaves us unable to extract our instances
# IP within its default network.

# the following line deletes the current ALLOWED_HOSTS line
sed -i '/ALLOWED_HOSTS/d' ./vbvb/settings.py
# the following line adds in a new ALLOWED_HOSTS line
sed -i "28iALLOWED_HOSTS = \['$EXTERNAL_IP', '127.0.0.1'\]" ./vbvb/settings.py

# start server
echo "INFORMATION TO USER FROM vasserballverband TEAM..."
echo "Jenkins admin password is... $JENKINS_ADMIN_PASSWORD"
echo "This is your external IP... $EXTERNAL_IP"
echo "Run this command 'python3 manage.py runserver 0.0.0.0:8000' to start server"
python3 manage.py runserver 0.0.0.0:8000


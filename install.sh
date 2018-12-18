#!/bin/bash
# */vasserballverband/vbvb/install.sh

# Update and upgrade
sudo apt update && sudo apt upgrade -y

# Python 3.6.7 is pre-installed on Ubuntu 18.04 so just install pip3 and tree
sudo apt install -y python3-pip tree

# Install all Django dependencies
sudo -H pip3 install django djangorestframework django_extensions

# git is pre-installed on ubuntu 18.04, do nothing
echo "All installations attempted"

# Cleanup
sudo apt autoremove

# We now want to
# change ALLOWED_HOSTS in */vasserballverband/vbvb/vbvb/settings.py to your instance's
# public IP. To get the public IP we have to use
EXTERNAL_IP=$(curl -H "Metadata-Flavor: Google" http://169.254.169.254/computeMetadata/v1/instance/network-interfaces/0/access-configs/0/external-ip)
# because GCP's virtualization of hardware leaves us unable to extract our instances
# IP within its default network.

# the following line deletes the current ALLOWED_HOSTS line
sed -i '/ALLOWED_HOSTS/d' ./vbvb/settings.py
# the following line adds in a new ALLOWED_HOSTS line
sed -i "28iALLOWED_HOSTS = \['$EXTERNAL_IP'\]" ./vbvb/settings.py

python3 manage.py runserver 0.0.0.0:8000


# vasserballverband
<domain name goes here>

An API platform for water polo.

Examples of applications you could build...
- Top 10 lists for NCAA, High School, and Club (one included)
- A Pool Cost comparison chart


## Tech Stack: Present and Future
* Backend  - `Python 3.6.*`, `Django 2.*`, `SQLite`, `django-rest-framework`, `PostgreSQL`
* Frontend - `Javascript`, `jQuery`, `AJAX`, `HTML`, `CSS`
* DevOps   - `GCP`, `AWS`, `Terraform`, `Jenkins`, `Ansible`, `Apache`, `Bash/Linux`, `Docker`, `Kubernetes`


## Install
```
# Spin up a GCP-CE instance, ensure it is Ubuntu 18.04 and allows HTTP(S) + Port 8000

# SSH into the instance

# install script
git clone https://github.com/JacobBHartman/vasserballverband
cd ~/vasserballverband/vbvb
../install.sh

# extract admin password for Jenkins
sudo docker logs jenkins_container 2>&1 | grep -A 2 "Please use the following" | tail -1
# go to Jenkins thru your browser, login and follow the prompt, install default plugins

# flush DB
cd ~/vasserballverband/vbvb
rm -Rf api/migrations/*
touch api/migrations/__init__.py
rm db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate
# python3 manage.py shell
# copy script into python3 shell
```


## Author and Meta
Jacob B. Hartman

This project had a grand re-opening on the 13th day of December in the year 2018 anno Domini Gregorian New Style.

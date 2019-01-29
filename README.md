# vasserballverband

An API platform for water polo.

[The API](http://www.wasserballver.band/api)

[Example app](http://www.wasserballver.band)



The API provides the following models...
* `Authority`: the legal entity in charge of a team, institution, or facility
* `City`: a locality, either a city, town, CDP or other (United States focused)
* `Finish`: the end finish for a team within a tournament or series
* `State`: one of the 50 United States of America. Could be generalized to `Subcountry`
* `Team`: A water polo team
* `Tournament`: A series or tournament of water polo games`
* Future: `Game`: an individual match of water polo
* Future: `People`: Including players, coaches, administrators, officials, etc.
* Future: `City`, `State`, and `County` could be condensed to `Place`.
* Future: `Pool`: A water polo pool

Examples of applications you could build...
- Top 10 lists for NCAA, High School, Club, etc.
- Best in State, Best in County, Best in City
- Best Cities for Water Polo based on their Club and High School Finishes plus the number of universities they have
- A Pool Cost comparison chart
- Water Polo Wiki
- Club-Administration-as-a-Service


## Tech Stack: Present and Future
* Backend  - `Python 3.6.*`, `Django 2.*`, `SQLite`, `django-rest-framework`
* Frontend - `HTML`, `CSS`
* DevOps   - `GCP`, `AWS`, `Terraform`, `Jenkins`, `Ansible`, `Bash/Linux`, `Docker`


## Installation (for devs)
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

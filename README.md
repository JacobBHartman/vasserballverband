# vasserballverband

This project had a grand re-opening on the 13th day of December in the year 2018 anno Domini Gregorian New Style.

This project was created by Jacob Hartman.

## For Employers and Recruiters
The stack used is Python, Django, SQLite, django-rest-framework, HTML, Terraform, Jenkins
The stack will be added to with Javascript Jquery AJAX, Apache, PostgresQL, Docker, Kubernetes, Ansible


## Description 

An API designed for water polo across all domains and countries. vasserballverband (vbvb) acts as a platform on top of which can be built any number of applications.

The example application included prints out The top teams from CIFSS D1+D2+D3.

The purpose of building this application(s) is to demonstrate proficiency, motivation, as well as personal reasons.

Expore the following...
  Variable names and files should have the noun first followed by adjectives. I.E. "cat black" or "gato negro" > "black cat"
  Avoid using abbreviations and acronyms as much as possible except where you state it outwardly: "Federal Bureau of Investigation (FBI)"... We want noobs to be able to read and understand the code as much as possible. Also people from the future. Also Non-english speakers.

Eventually the site(s) should have the following attributes...
* Optimized installation with as few steps as possible
* Sexy domain names, subdomains
* Firewall
* Containerized
* Fully tested

The eventual tech stack will be...
* Python 3.6*
* Django 2*
* PostgreSQL
* HTML+CSS+JS
* Apache
built on AWS.

Supporting documents will include...
* Terraformed
* Jenkins
* Docker+K8s
* AWS
* Ansible

## Install
```
# Spin up a GCP-CE instance, ensure it is Ubuntu 18.04 and allows HTTP(S) + Port 8000

# SSH into the instance

# install script
git clone https://github.com/JacobBHartman/vasserballverband
cd ~/vasserballverband/vbvb
../install.sh

# extract admin password
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


## Personal log
#### 13th Day of December, 2018
One of the greatest lessons I learned was to make an MVP. I ought to never forget this lesson and yet I continuous shoot too high too soon. Therefore, I will make a concerted effort to keep-it-simple-stupid early and often while making this project. For an MVP, I should get a site live locally. The site should be a Top 10 app of 12U, 14U, 16U and 18U boys water polo teams in Southern California.

The site should use Python, Django, Postgres, HTML+CSS+JS on AWS and Apache.

I should focus on the Django and Postgres up-front.

#### 16th Day of December, 2018
So far I've managed to scrap together a very production-unfriendlyAPI with no front-end but it works. I have a simple table. Now I need to create an app front-end that will communicate with my api.

Mid-day update: I now have an application called TOP_CIFSS that is separate from my API. As of now they run on the same server. I shall detail the interactions between my apps before I move on. Also, before the end of the day I should get a basic installation instructions put together.

#### 18th Day of December, 2018
So now I have an easy to use install script that can spin up a GCP instance ASAP. I needed this because I want to be able to start from scratch each time I come in to work.

#### 28th Day of December, 2018
I need to get an app running as quick as possible. Let's do Top 10 Socal 18U at Junior Olympics
To do that I need to have a public database that can be modfied a la Wikipedia style, i.e. publically. The public database will take the form of a CSV file that can be parsed to quickly create instances of models.
Once I create the parser and successfuly convert the public CSV file to my application DB, I can create the front-end and have it permanent.

###

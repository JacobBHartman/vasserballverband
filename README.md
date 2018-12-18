# vasserballverband

This project had a grand re-opening on the 13th day of December in the year 2018 anno Domini Gregorian New Style.

This project was created by Jacob Hartman.

## Description 

An API designed for water polo across all domains and countries. vasserballverband (vbvb) acts as a platform on top of which can be built any number of applications.

The example application included prints out The top teams from CIFSS D1+D2+D3.

The purpose of building this application(s) is to demonstrate proficiency, motivation, as well as personal reasons.

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

git clone https://github.com/JacobBHartman/vasserballverband
cd ~/vasserballverband/vbvb
../install.sh
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

# Development Journal


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

####

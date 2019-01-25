#!/usr/bin/env python3
'''
    Run within Python shell after running 'python3 manage.py shell'

    This Python script will convert comma-separated-values (.csv) files, each of which corresponds to a model in the application programming interface (API).

    Its first task is to rename .csv files downloaded from the public Google Sheets
    spreadsheet into a sanitized .csv file that mimics its corresponding models name.

    Its second task is to open each file and write objects one-by-one to the database. Files have to be opened and used to populate the database in a specific order. That specific order is in order of dependence. Least dependent models are populated first, most dependent models are populated last

    It would be nice if there were a program that automatically wrote models from .csv files but I guess that is another project in itself.
'''
from api.models import Authority, City, Finish, State, Team, Tournament
from csv import DictReader
from django.utils import timezone
from django.utils.text import slugify
from os import rename
from uuid import uuid4


# Rename all the .csv files with unsanitary names
prefix = 'water_polo_public_data - ' # file prefix
words = ['authorities', 'cities', 'finishes', 'teams', 'tournaments', 'states']
for word in words:
    word += '.csv'
    rename('populate/'+prefix+word, 'populate/'+word)


# Now populate the database with objects based on the .csv file
with open('./populate/authorities.csv') as c:
    r = DictReader(c)
    for row in r:
        p = Authority(created=timezone.now(),
                      modified=timezone.now(),
                      uid=uuid4(),
                      name=row['name'],
                      slug=slugify(row['name']),
                      kind=row['kind'],)
        p.save()

with open('./populate/states.csv') as c:
    r = DictReader(c)
    for row in r:
        p = State(created=timezone.now(),
                  modified=timezone.now(),
                  uid=uuid4(),
                  name=row['name'],
                  abbreviation=row['abbreviation'],
                  population=int(row['population_2017'].replace(',', '')),
                  slug=slugify(row['name']),)
        p.save()

with open('./populate/tournaments.csv') as c:
    r = DictReader(c)
    for row in r:
        p = Tournament(created=timezone.now(),
                       modified=timezone.now(),
                       uid=uuid4(),
                       name=row['name'],
                       slug=slugify(row['name']),
                       number_of_teams=int(row['number_of_teams']),)
        p.save()

with open('./populate/cities.csv') as c:
    r = DictReader(c)
    state = State.states.get(name__iexact='California')
    for row in r:
        p = City(created=timezone.now(),
                 modified=timezone.now(),
                 uid=uuid4(),
                 name=row['name'],
                 state=State.states.get(name__iexact=row['name_state']),
                 slug=slugify(row['name']+row['name_state']),)
        p.save()

with open('./populate/teams.csv') as c:
    r = DictReader(c)
    for row in r:
        city      = City.cities.get(name__iexact=row['name_city'])
        authority = Authority.authorities.get(name__iexact=row['name_authority'])
        p = Team(created=timezone.now(),
                 modified=timezone.now(),
                 uid=uuid4(),
                 name=row['name'],
                 city=city,
                 authority=authority,
                 kind=row['kind'],
                 slug=slugify(row['name']),)
        p.save()

with open('./populate/finishes.csv') as c:
    r = DictReader(c)
    for row in r:
        tournament = Tournament.tournaments.get(name__iexact=row['name_tournament'])
        team       = Team.teams.get(name__iexact=row['name_team'])
        p = Team(created=timezone.now(),
                 modified=timezone.now(),
                 uid=uuid4(),
                 tournament=tournament,
                 team=team,
                 finish=int(row['place']),)
        p.save()


#!/bin/env/python3
'''
    Run within Python shell after running 'python3 manage.py shell'
'''

from csv import DictReader
from api.models import City, State
from django.utils import timezone
from uuid import uuid4

with open('api/states.csv') as c:
    r = DictReader(c)
    for row in r:
        p = State(created=timezone.now(),
                  modified=timezone.now(),
                  uid=uuid4(),
                  name=row['name'],
                  abbreviation=row['abbreviation'],
                  population=int(row['population_2017'].replace(',', '')),)
        p.save()

with open('api/cities.csv') as c:
    r = DictReader(c)
    state = State.states.get(name__iexact='California')
    for row in r:
        p = City(created=timezone.now(),
                 modified=timezone.now(),
                 uid=uuid4(),
                 name=row['name'],
                 state_id=state,)
        p.save()

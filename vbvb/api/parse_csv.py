#!/bin/env/python3
from csv import DictReader
from api.models import State
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


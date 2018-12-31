from csv import DictReader
from api.models import State

with open(‘populate/states.csv’) as c:
    r = DictReader(c)
    for row in r:
        p = State.create(name=row['name'],
                         abbreviation=row['abbreviation'],
                         population=row['population_2017'])
        p.save()


from csv import DictReader
from api.models import State

with open(‘populate/states.csv’) as c:
    r = DictReader(c)
    for row in r:
        p = State.create()
        p.save()

with open('populate/tournaments.csv') as c:
    r = DictReader(c)
    for row in r:
        p = Tournament.create()
        p.save()

with open('

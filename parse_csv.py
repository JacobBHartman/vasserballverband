from csv import DictReader
from os import chdir

path = ''

chdir(path)

from api.models import State

with open('water_polo_public_data - states.csv') as csv_file:
    reader = DictReader(csv_file)
    for row in reader:
        p = State(name=row['name'])
        p.save()



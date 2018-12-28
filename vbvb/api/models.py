from django.db import models

from uuid import uuid4

from django.db.models import Model, UUIDField
from django.db.models import CharField, TextField, SlugField, CASCADE
from django.db.models import IntegerField, DateTimeField, ForeignKey

class BaseModel(Model):
    unique_id = UUIDField(primary_key=True,
                          default=uuid4,
                          editable=False,
                          unique=True)
    created = DateTimeField()
    modified = DateTimeField()

class Team(BaseModel):
    def __str__(self):
        return self.team_text
    
    name = CharField(max_length=80)
    team_text = CharField(max_length=200, default="default_team_text")
    description = TextField()
    club_id = ForeignKey(Club, on_delete=CASCADE)
    kind = CharField(max_length=40)

class City(BaseModel):
    name = CharField(max_length=80)
    state_id = ForeignKey(State, on_delete=CASCADE)

class State(BaseModel):
    name = CharField(max_length=80)

class Club(BaseModel):
    name = CharField(max_length=80)
    city_id = ForeignKey(City, on_delete=CASCADE)

class Tournament(BaseModel):
    name = CharField(max_length=80)
    number_of_teams = IntegerField()

class Finish(BaseModel):
    team_id = ForeignKey(Team, on_delete=CASCADE)
    tournament_id = ForeignKey(Tournament, on_delete=CASCADE)
    finish = IntegerField()
    



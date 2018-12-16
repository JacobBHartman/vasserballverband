from django.db import models

# Create your models here.
from django.db.models import Model
from django.db.models import CharField, TextField, SlugField, CASCADE
from django.db.models import IntegerField, DateTimeField, ForeignKey

class Team(Model):
    def __str__(self):
        return self.team_text
    
    name = CharField(max_length=80)
    team_text = CharField(max_length=200, default="hi")
    description = TextField()
    city = CharField(max_length=80)
    state = CharField(max_length=20)
    kind = CharField(max_length=40)
    place = IntegerField()
    created = DateTimeField()
    modified = DateTimeField()

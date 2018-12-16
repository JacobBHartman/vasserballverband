from django.db import models

# Create your models here.
from django.db.models import Model
from django.db.models import CharField, TextField, SlugField, CASCADE
from django.db.models import IntegerField, DateTimeField, ForeignKey

class Team(Model):
    name = CharField(max_length=80)
    description = TextField()
    city = CharField(max_length=80)
    state = CharField(max_length=20)
    kind = CharField(max_length=40)
    place = IntegerField()
    created = DateTimeField()
    modified = DateTimeField()

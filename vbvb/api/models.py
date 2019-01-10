# */vasserballverband/vbvb/api/models.py


from django.db.models import CASCADE, ForeignKey, Manager, Model
from django.db.models import CharField, DateTimeField, IntegerField, SlugField
from django.db.models import TextField, UUIDField

from django.utils import timezone
from django.utils.text import slugify
from pytz import UTC
from uuid import uuid4


# BaseModel is a universal parent class
class BaseModel(Model):
    uid         = UUIDField(primary_key=True,
                            default=uuid4(),
                            editable=False,
                            unique=True)
    created     = DateTimeField(auto_now_add=True,
                                editable=False,
                                blank=False)
    modified    = DateTimeField(auto_now=True,
                                blank=False)
    base_models = Manager()
    class Meta:
        abstract=True


# Models without a dependency on other models
class State(BaseModel):
    name         = CharField(default='Iraq',
                             unique=True,
                             max_length=80)
    slug         = SlugField(unique=True)
    abbreviation = CharField(default='IQ',
                             unique=True,
                             max_length=2)
    population   = IntegerField(default=1)
    states       = Manager()

    class Meta:
        ordering = ('name',)


class Authority(BaseModel):
    name        = CharField(max_length=80)
    slug        = SlugField(unique=True)
    kind        = CharField(max_length=40)
    authorities = Manager()

    class Meta:
        ordering = ('name',)


class Tournament(BaseModel):
    name            = CharField(max_length=80)
    slug            = SlugField(unique=True)
    number_of_teams = IntegerField(default=2) #this can be insinuated by gathering teams from finishes
    tournaments     = Manager()


# Models with a dependency on the above models
class City(BaseModel):
    name   = CharField(max_length=80)
    slug   = SlugField(unique=True)
    state  = ForeignKey(State,
                        related_name='cities',
                        on_delete=CASCADE)
    cities = Manager()

    class Meta:
        ordering        = ['name']
        unique_together = ('name', 'state')


# Models with a dependency on the above models
class Team(BaseModel):
    name      = CharField(max_length=80)
    slug      = SlugField(unique=True)
    authority = ForeignKey(Authority,
                           related_name='teams',
                           on_delete=CASCADE)
    city      = ForeignKey(City,
                           related_name='teams',
                           on_delete=CASCADE)
    kind      = CharField(max_length=40)
    teams     = Manager()

    class Meta:
        ordering        = ['name']
        unique_together = ('name', 'authority', 'kind')


# Models with a dependency on the above models
class Finish(BaseModel):
    team       = ForeignKey(Team,
                            related_name='finishes',
                            on_delete=CASCADE)
    tournament = ForeignKey(Tournament,
                            related_name='finishes',
                            on_delete=CASCADE)
    place      = IntegerField()
    finishes   = Manager()


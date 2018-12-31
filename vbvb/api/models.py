from django.db.models import Manager, Model, UUIDField
from django.db.models import CharField, TextField, SlugField, CASCADE
from django.db.models import IntegerField, DateTimeField, ForeignKey

from django.utils import timezone
from pytz import UTC

from uuid import uuid4

class BaseModel(Model):
    uid = UUIDField(primary_key=True,
                    default=uuid4(),
                    editable=False,
                    unique=True)
    created = DateTimeField(auto_now_add=True,
                            editable=False,
                            blank=False)
    modified = DateTimeField(auto_now=True,
                             blank=False)
    
    class Meta:
        abstract=True

    objects = BaseModelManager()


# Models without a dependency on other models
class State(BaseModel):
    name            = CharField(max_length=80)
    abbreviation    = CharField(max_length=2)
    population_2017 = IntegerField()

    objects = StateManager()

'''
class Tournament(BaseModel):
    name = CharField(max_length=80)
    number_of_teams = IntegerField()


# Models with a dependency on the above models
class City(BaseModel):
    name = CharField(max_length=80)
    state_id = ForeignKey(State, on_delete=CASCADE)

# Models with a dependency on the above models
class Club(BaseModel):
    name = CharField(max_length=80)
    city_id = ForeignKey(City, on_delete=CASCADE)

# Models with a dependency on the above models
class Team(BaseModel):
    def __str__(self):
        return self.team_text
    
    name = CharField(max_length=80)
    team_text = CharField(max_length=200, default="default_team_text")
    description = TextField()
    club_id = ForeignKey(Club, on_delete=CASCADE)
    kind = CharField(max_length=40)

# Models with a dependency on the above models
class Finish(BaseModel):
    team_id = ForeignKey(Team, on_delete=CASCADE)
    tournament_id = ForeignKey(Tournament, on_delete=CASCADE)
    place = IntegerField()
    '''

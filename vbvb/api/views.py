from . import views
from .models import Authority, City, Finish, State, Team, Tournament

from .serializers import AuthoritySerializer, CitySerializer
from .serializers import FinishSerializer, StateSerializer
from .serializers import TeamSerializer, TournamentSerializer

from rest_framework.viewsets import ModelViewSet


class AuthorityViewSet(ModelViewSet):
    serializer_class = AuthoritySerializer
    queryset = Authority.authorities.all()
    lookup_field = 'slug'


class CityViewSet(ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.cities.all()
    lookup_field = 'slug'


class FinishViewSet(ModelViewSet):
    serializer_class = FinishSerializer
    queryset = Finish.finishes.all()


class StateViewSet(ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.states.all()
    lookup_field = 'slug'


class TeamViewSet(ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.teams.all()
    lookup_field = 'slug'


class TournamentViewSet(ModelViewSet):
    serializer_class = TournamentSerializer
    queryset = Tournament.tournaments.all()
    lookup_field = 'slug'

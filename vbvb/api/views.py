from . import views
from .models import Authority, City, Finish, State, Team, Tournament

from .serializers import AuthoritySerializer, CitySerializer
from .serializers import FinishSerializer, StateSerializer
from .serializers import TeamSerializer, TournamentSerializer

from rest_framework.viewsets import ModelViewSet


class AuthorityViewSet(ModelViewSet):
    serializer_class = AuthoritySerializer
    queryset = Authority.authorities.all()


class CityViewSet(ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.cities.all()


class FinishViewSet(ModelViewSet):
    serializer_class = FinishSerializer
    queryset = Finish.finishes.all()


class StateViewSet(ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.states.all()


class TeamViewSet(ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.teams.all()


class TournamentViewSet(ModelViewSet):
    serializer_class = TournamentSerializer
    queryset = Tournament.tournaments.all()


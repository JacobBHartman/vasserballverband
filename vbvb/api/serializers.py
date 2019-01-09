# */vasserballverband/vbvb/api/models.py
'''
    Description: From django-rest-framework.org... "
'''


from rest_framework.serializers import ModelSerializer
from .models import Authority, City, Finish, State, Team, Tournament


class AuthoritySerializer(ModelSerializer):
    class Meta:
        model  = Authority
        fields = '__all__'


class CitySerializer(ModelSerializer):
    class Meta:
        model  = City
        fields = '__all__'


class FinishSerializer(ModelSerializer):
    class Meta:
        model  = Finish
        fields = '__all__'


class StateSerializer(ModelSerializer):
    class Meta:
        model  = State
        fields = '__all__'


class TeamSerializer(ModelSerializer):
    class Meta:
        model  = Team
        fields = '__all__'


class TournamentSerializer(ModelSerializer):
    class Meta:
        model  = Tournament
        fields = '__all__'


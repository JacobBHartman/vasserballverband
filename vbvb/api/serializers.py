# */vasserballverband/vbvb/api/models.py
'''
    Description: From django-rest-framework.org... "
'''


from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField
from .models import Authority, City, Finish, State, Team, Tournament


class AuthoritySerializer(ModelSerializer):
    teams = HyperlinkedRelatedField(
                many=True,
                read_only=True,
                view_name='team-detail'
            )
    class Meta:
        model  = Authority
        fields = '__all__'


class CitySerializer(ModelSerializer):
    teams = HyperlinkedRelatedField(
                many=True,
                read_only=True,
                view_name='team-detail'
            )
    class Meta:
        model  = City
        fields = '__all__'


class FinishSerializer(ModelSerializer):
    class Meta:
        model  = Finish
        fields = '__all__'


class StateSerializer(ModelSerializer):
    cities = HyperlinkedRelatedField(
                 many=True,
                 read_only=True,
                 view_name='city-detail'
             )
    class Meta:
        model  = State
        fields = '__all__'


class TeamSerializer(ModelSerializer):
    finishes = HyperlinkedRelatedField(
                   many=True,
                   read_only=True,
                   view_name='finish-detail'
               )
    class Meta:
        model  = Team
        fields = '__all__'


class TournamentSerializer(ModelSerializer):
    finishes = HyperlinkedRelatedField(
                   many=True,
                   read_only=True,
                   view_name='finish-detail'
               )
    class Meta:
        model  = Tournament
        fields = '__all__'


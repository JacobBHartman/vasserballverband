# */vasserballverband/vbvb/api/models.py
'''
    Description: From django-rest-framework.org... "
'''


from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.serializers import HyperlinkedRelatedField
from rest_framework.serializers import HyperlinkedIdentityField

from .models import Authority, City, Finish, State, Team, Tournament


class AuthoritySerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='authority-detail',
        lookup_field='slug'
    )
    teams = HyperlinkedRelatedField(
        view_name='team-detail',
        lookup_field='slug',
        many=True,
        read_only=True
    )
    
    class Meta:
        model  = Authority
        fields = '__all__'


class CitySerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='city-detail',
        lookup_field='slug'
    )
    teams = HyperlinkedRelatedField(
        view_name='team-detail',
        lookup_field='slug',
        many=True,
        read_only=True
    )

    class Meta:
        model  = City
        fields = '__all__'


class FinishSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='finish-detail'
    )
    class Meta:
        model  = Finish
        fields = '__all__'


class StateSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='state-detail',
        lookup_field='slug'
    )
    cities = HyperlinkedRelatedField(
        view_name='city-detail',
        lookup_field='slug',
        many=True,
        read_only=True
    )
    
    class Meta:
        model  = State
        fields = '__all__'


class TeamSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='team-detail',
        lookup_field='slug'
    )
    finishes = HyperlinkedRelatedField(
        view_name='finish-detail',
        lookup_field='tournament',
        many=True,
        read_only=True
    )
    
    class Meta:
        model  = Team
        fields = '__all__'


class TournamentSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='tournament-detail',
        lookup_field='slug'
    )
    finishes = HyperlinkedRelatedField(
        view_name='finish-detail',
        lookup_field='team',
        many=True,
        read_only=True
    )
    
    class Meta:
        model  = Tournament
        fields = '__all__'

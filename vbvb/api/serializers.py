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

        #fields = ('uid', 'created', 'modified')i
        fields = ('uid', 'created', 'modified', 'name', 'slug', 'kind', 'url', 'teams')

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
    state = HyperlinkedRelatedField(
        view_name='state-detail',
        read_only=True,
        lookup_field='slug'
    )
    class Meta:
        model  = City
        fields = ('uid', 'created', 'modified', 'name', 'slug', 'state', 'url', 'teams')


class FinishSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='finish-detail',
        lookup_field='slug'
    )
    team = HyperlinkedRelatedField(
        view_name='team-detail',
        read_only=True,
        lookup_field='slug',
    )
    tournament = HyperlinkedRelatedField(
        view_name='tournament-detail',
        read_only=True,
        lookup_field='slug'
    )
    class Meta:
        model  = Finish
        fields = ('uid', 'created', 'modified', 'team', 'tournament', 'place', 'url', 'slug')


class StateSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='state-detail',
        lookup_field='slug',
    )
    cities = HyperlinkedRelatedField(
        view_name='city-detail',
        lookup_field='slug',
        many=True,
        read_only=True
    )
  
    
    class Meta:
        model  = State
        fields = ('uid', 'created', 'modified', 'name', 'slug', 'abbreviation', 'population', 'url', 'cities')


class TeamSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='team-detail',
        lookup_field='slug'
    )
    finishes = HyperlinkedRelatedField(
        view_name='finish-detail',
        lookup_field='slug',
        many=True,
        read_only=True
    )
    authority = HyperlinkedRelatedField(
        read_only=True,
        view_name='authority-detail',
        lookup_field='slug'
    )
    city = HyperlinkedRelatedField(
        read_only=True,
        view_name='city-detail',
        lookup_field='slug'
    )
    
    class Meta:
        model  = Team
        fields = ('authority', 'city', 'uid', 'created', 'modified', 'name', 'slug', 'kind', 'url', 'finishes')
        # 'authority', 'city'
        '''
            So I've had a breakthrough discovery. When I put in the two
            parent models as fields for team, it would attempt to
            resolve the detail of that authority or city rather than
            just providing the URL for them. let's see if I can
            get the urls instead
        '''

class TournamentSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='tournament-detail',
        lookup_field='slug'
    )
    finishes = HyperlinkedRelatedField(
        view_name='finish-detail',
        lookup_field='slug',
        many=True,
        read_only=True
    )
    
    class Meta:
        model  = Tournament
        fields = ('uid', 'created', 'modified', 'name', 'slug', 'number_of_teams', 'url', 'finishes')

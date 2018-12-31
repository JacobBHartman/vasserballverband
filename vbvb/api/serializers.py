from rest_framework.serializers import ModelSerializer
from .models import State, Team

class StateSerializer(ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
'''
class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'description', 'city', 'state', 'kind', 'place', 'created', 'modified')

class TeamSummarySerializer(ModelSerializer):
    class Meta:
        model = models.Team
        fields = ('name', 'place')
        '''

from rest_framework import serializers
from . import models


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = ('name', 'description', 'city', 'state', 'kind', 'place', 'created', 'modified')

class TeamSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = ('name', 'place')

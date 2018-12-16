from rest_framework import viewsets
from . import serializers
from . import models

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TeamSerializer
    queryset = models.Team.objects.all()
# Create your views here.

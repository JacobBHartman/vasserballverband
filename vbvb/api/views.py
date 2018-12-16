from . import serializers
from . import models
from . import views

from rest_framework import viewsets


class TeamViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.TeamSummarySerializer

        return serializers.TeamSerializer

from . import views
from .models import State
from .serializers import StateSerializer

from rest_framework import viewsets


class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.states.all()
'''
class StateList(generics.ListCreateAPIView):
    queryset = State.states.all()
    serializer_class = StateSerializer

class StateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.states.all()
    serializer_class = StateSerializer
'''
'''
class CreateView(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

    def perform_create(self, serializer):
        serializer.save()

class TeamViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.TeamSummarySerializer

        return serializers.TeamSerializer'''

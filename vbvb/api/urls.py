from .views import AuthorityViewSet, CityViewSet, FinishViewSet
from .views import StateViewSet, TeamViewSet, TournamentViewSet

from django.urls import include, path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('authorities', AuthorityViewSet)
router.register('cities',      CityViewSet)
router.register('finishes',    FinishViewSet)
router.register('states',      StateViewSet)
router.register('teams',       TeamViewSet)
router.register('tournaments', TournamentViewSet)


urlpatterns = [
    path('', include(router.urls))
]

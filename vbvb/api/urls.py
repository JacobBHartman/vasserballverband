from .views import StateViewSet

from django.urls import include, path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('states', StateDetails)

urlpatterns = [
    path('', include(router.urls))
]

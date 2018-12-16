from django.urls import path, include
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()

# router.register('app', views.index)

urlpatterns = [
    path('', views.index, name='index')
]


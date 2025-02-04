from Station.views import getAllStation, getStation
from django.urls import path

urlpatterns = [
    path('station', getAllStation),
    path('station/<int:no>', getStation)
]
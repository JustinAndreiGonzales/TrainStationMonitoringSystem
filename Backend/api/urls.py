from Station.views import get_all_station, get_station
from django.urls import path

urlpatterns = [
    path('station/', get_all_station, name="station-list"),
    path('station/<int:id>/', get_station, name="station-details")
]
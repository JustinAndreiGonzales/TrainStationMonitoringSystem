from Station.views import get_all_station, get_station
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from Users.views import SignUpView, CustomTokenObtainPairView

urlpatterns = [
    # stations
    path('station/', get_all_station, name="station-list"),
    path('station/<int:id>/', get_station, name="station-details"),

    # admin
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    # annoucements

    # reports

    # calculator
]
from Station.views import get_all_station, get_station, ProtectedView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView
from Users.views import SignUpView, CustomTokenObtainPairView

urlpatterns = [
    # stations
    path('station/', get_all_station, name="station-list"),
    path('station/<int:id>/', get_station, name="station-details"),

    # admin
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/logout/', TokenBlacklistView.as_view(), name='logout'),

    # annoucements

    # reports

    # calculator

    path('test/', ProtectedView.as_view(), name='test')
]
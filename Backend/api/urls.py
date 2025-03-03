from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView

from Station.views import get_all_station, get_station, ProtectedView, get_cctv_feed
from Users.views import SignUpView, CustomTokenObtainPairView
from Announcements.views import AnnouncementListView
from Reports.views import ReportsListView

urlpatterns = [
    # stations
    path('station/', get_all_station, name="station-list"),
    path('station/<int:id>/', get_station, name="station-details"),
    # station cctv feed
    path("station/<int:id>/cctv_feed/<str:platform_side>", get_cctv_feed, name="cctv_feed"),

    # admin
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/logout/', TokenBlacklistView.as_view(), name='logout'),

    # annoucements
    path('announcements/', AnnouncementListView.as_view(), name='announcements'),
    # GET /announcements/?limit=3&offset=0 (limit - # to get, offset - index to start)

    # reports
    path('reports/', ReportsListView.as_view(), name='reports'),
    # GET /reports/?limit=3&offset=0 (limit - # to get, offset - index to start)

    # calculator

    path('test/', ProtectedView.as_view(), name='test')
]

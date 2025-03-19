from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView

from Station.views import get_all_station, get_station, ProtectedView, get_cctv_feed, get_hourly_density, get_daily_density, get_current_density
from Users.views import SignUpView, CustomTokenObtainPairView
from Announcements.views import AnnouncementListView, AnnouncementCreateView, AnnouncementGetView, AnnouncementUpdateView
from Reports.views import ReportsListView, ReportSumbitView
from RouteFinding.views import route_finding

urlpatterns = [
    # stations
    path('station/', get_all_station, name="station-list"),
    path('station/<int:id>/', get_station, name="station-details"),
    # station cctv feed
    # path('station/<int:id>/cctv-feed/', get_cctv_feed, name="cctv-feed"),
    path('station/<int:id>/cctv-feed/<str:platform_side>', get_cctv_feed, name="cctv-feed"),

    # density
    path('station/<int:id>/current-density/<str:platform_side>', get_current_density, name="current-density"),
    path('station/<int:id>/hourly-density/<str:platform_side>', get_hourly_density, name="hourly-density"),
    path('station/<int:id>/daily-density/<str:platform_side>', get_daily_density, name="daily-density"),

    # admin
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/logout/', TokenBlacklistView.as_view(), name='logout'),

    # annoucements
    path('announcements/', AnnouncementListView.as_view(), name='announcements'),
    path('announcements/<int:pk>', AnnouncementGetView.as_view(), name="announcements-get"),
    path('announcements/create/', AnnouncementCreateView.as_view(), name="annoucements-create"),
    path('announcements/update/<int:pk>', AnnouncementUpdateView.as_view(), name="announcements-update"),
    # GET /announcements/?limit=3&offset=0 (limit - # to get, offset - index to start)

    # reports
    path('reports/', ReportsListView.as_view(), name='reports'),
    # GET /reports/?limit=3&offset=0 (limit - # to get, offset - index to start)
    path('reports/create/', ReportSumbitView.as_view(), name='report-submission'),

    # calculator
    path('route/<int:src>/<int:dest>/', route_finding, name='route-finding'),

    path('test/', ProtectedView.as_view(), name='test')
]

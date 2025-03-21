from django.urls import re_path
from .consumers import TrainETAConsumer

websocket_urlpatterns = [
    re_path(r"ws/eta/(?P<station_id>\d+)/(?P<platform_side>\w+)/$", TrainETAConsumer.as_asgi()),
]

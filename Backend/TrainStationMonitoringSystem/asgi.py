"""
ASGI config for TrainStationMonitoringSystem project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
import Station.routing  # Replace "your_app" with your actual app name

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TrainStationMonitoringSystem.settings")

# application = ProtocolTypeRouter(
#     {
#         "http": get_asgi_application(),  # Handles HTTP requests
#         "websocket": URLRouter(Station.routing.websocket_urlpatterns),  # Handles WebSockets
#     }
# )

application = ProtocolTypeRouter({
    "https": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                Station.routing.websocket_urlpatterns
            )
        ),
    ),
})

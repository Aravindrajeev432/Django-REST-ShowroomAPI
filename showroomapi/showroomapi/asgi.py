"""
ASGI config for showroomapi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

from requests.consumers import RequestConsumer
from users.consumers import UserNotificationConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'showroomapi.settings')

django_asgi_app = get_asgi_application()
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': URLRouter(
        [
            re_path(r'ws/request-server', RequestConsumer.as_asgi()),
            re_path(r'ws/user-notifications/(?P<room_name>\w+)$', UserNotificationConsumer.as_asgi()),
        ])
    # Just HTTP for now. (We can add other protocols later.)
})

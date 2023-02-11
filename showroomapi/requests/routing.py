from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
    re_path(r'ws/request-server', consumers.RequestConsumer.as_asgi()),
]
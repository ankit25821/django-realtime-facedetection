from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/', consumers.DefaultConsumer.as_asgi()),
]
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("wss/chat/<int:chatroom_id>/", consumers.ChatConsumer.as_asgi()),
]

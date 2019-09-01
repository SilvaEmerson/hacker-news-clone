from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from hackernewsclone.consumers import PostConsumer

application = ProtocolTypeRouter(
    {
        # (http->django views is added by default)
        "websocket": URLRouter([path("ws/posts/<str:author>/", PostConsumer)])
    }
)

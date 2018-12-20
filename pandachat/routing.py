from django.urls import re_path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from chatserver.consumers import ChatConsumer

application = ProtocolTypeRouter(
    {"websocket": AuthMiddlewareStack(URLRouter([re_path(r"^ws/$", ChatConsumer)]))}
)

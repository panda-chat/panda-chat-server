from django.urls import re_path
from channels.sessions import SessionMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from chatserver.consumers import ChatConsumer

application = ProtocolTypeRouter(
    {"websocket": SessionMiddlewareStack(URLRouter([re_path(r"^ws/$", ChatConsumer)]))}
)

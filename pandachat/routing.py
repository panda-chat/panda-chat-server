from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from chatserver.consumers import ChatConsumer

application = ProtocolTypeRouter(
    {"websocket": AuthMiddlewareStack(URLRouter([url(r"^chat/$", ChatConsumer)]))}
)

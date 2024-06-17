import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import Omboli.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chats.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            Omboli.routing.websocket_urlpatterns
        )
    )
})
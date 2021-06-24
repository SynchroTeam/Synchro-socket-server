
import os

from django.core.asgi import get_asgi_application

from channels.sessions import SessionMiddlewareStack
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from Socket.urls import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django.settings')

application = ProtocolTypeRouter({
    'websocket': SessionMiddlewareStack(
        URLRouter(
            ws_urlpatterns
        )
    )
})

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# import chat.routing

# application = ProtocolTypeRouter({
#     # (http->django views is added by default)
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             chat.routing.websocket_urlpatterns
#         )
#     ),
# })
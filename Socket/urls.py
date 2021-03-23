from django.urls import path

# Create your views here.
# from .views import index

from .user import WSUser

ws_urlpatterns = [
    path('ws/some_url/<ID>/<USER_JWT>/<BLUEPRINT>/<connection_id>/', WSUser.as_asgi())
]
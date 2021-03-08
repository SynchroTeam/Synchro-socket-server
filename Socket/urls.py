from django.urls import path

# Create your views here.
# from .views import index

from .user import WSUser

ws_urlpatterns = [
    path('ws/some_url/<uri>/<ua>/<b>/', WSUser.as_asgi())
]

from django.urls import path, include
from .views import create_user, nice


urlpatterns = [
    path('create/', create_user, name="signup"),
    path('nice/', nice, name="nice")
]
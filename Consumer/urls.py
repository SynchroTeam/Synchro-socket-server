
from django.urls import path, include
from .views import get_tokens_for_user


urlpatterns = [
    path('v0/consumer/login/', get_tokens_for_user, name="signup")
]
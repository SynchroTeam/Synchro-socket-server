
from django.urls import path, include
from .views import get_tokens_for_user


urlpatterns = [
    path('login/', get_tokens_for_user, name="signup")
]
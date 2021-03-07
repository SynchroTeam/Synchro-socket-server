
from django.urls import path, include
from .views import CreateChannel


urlpatterns = [
    path('create/', CreateChannel, name="create_channel")
]
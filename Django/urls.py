"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v0/consumer/', include('Consumer.urls'), name="Consumer"),
    path('api/v0/channel/', include('Channel.urls'), name="Channel"),
    path('api/v0/user/', include('User.urls'), name="User"),
    path('docs/', include_docs_urls(title='API DOC')),
    path('schema', get_schema_view(
            title="BlogAPI",
            description="API for all things ...",
            version="1.0.0",
        ), name='openapi-schema'
    )
]
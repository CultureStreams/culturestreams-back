from django.urls import path, include
from . import views
from .routers import router
from rest_framework import routers
from rest_framework.authtoken import views

urlpatterns = [
    path('api/v0/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth')
]

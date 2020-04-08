from django.urls import path, include
from .routers import router

urlpatterns = [
    path('', include(router.urls)),
    #path('api-token-auth/', views.obtain_auth_token, name='api-token-auth')
]

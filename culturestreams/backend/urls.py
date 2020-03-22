from django.urls import path, include
from . import views
from rest_framework import routers

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
router = routers.DefaultRouter()
router.register('events', views.EventView)
router.register('plattforms', views.PlattformView)
router.register('categories', views.CategoryView)
router.register('tags', views.TagView)
urlpatterns = [
    path('', include(router.urls))
]

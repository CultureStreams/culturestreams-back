from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('events', views.EventView)
router.register('plattforms', views.PlattformView)
router.register('categories', views.CategoryView)
router.register('tags', views.TagView)
router.register('organizers', views.OrganizerView)

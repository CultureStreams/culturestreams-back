from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('events', views.EventView)
router.register('channels', views.ChannelView)
router.register('categories', views.CategoryView)
router.register('tags', views.TagView)
router.register('organizers', views.OrganizerView)
router.register('associates', views.AssociateView)

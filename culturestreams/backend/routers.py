from rest_framework import routers
#from .views import EventViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('events', views.EventViewSet)
router.register('plattforms', views.PlattformViewSet)
router.register('categories', views.CategoryViewSet)
router.register('tags', views.TagViewSet)
router.register('organizers', views.OrganizerViewSet)
router.register('subcategories', views.SubCategoryViewSet)

from rest_framework import routers
#from .views import EventViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'plattforms', PlattformViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)

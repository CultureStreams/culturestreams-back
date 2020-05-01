from rest_framework import viewsets
from django_filters import rest_framework as filters
from backend.models import Category, Event, Channel, Organizer
from .serializers import EventSerializer, ChannelSerializer, CategorySerializer, OrganizerSerializer, TagSerializer
from .serializers import EventReadSerializer, ChannelReadSerializer, OrganizerReadSerializer
from .filters import EventFilter, ChannelFilter, OrganizerFilter, CategoryFilter, TagFilter
from .renderers import CustomJSONRenderer
from taggit.models import Tag

class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filterset_class = TagFilter
    renderer_classes = [CustomJSONRenderer]

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter
    renderer_classes = [CustomJSONRenderer]

class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_class = EventFilter
    renderer_classes = [CustomJSONRenderer]
    def get_serializer_class(self):
         if self.request.method in ['GET']:
             return EventReadSerializer
         return EventSerializer

class ChannelView(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    filterset_class = ChannelFilter
    renderer_classes = [CustomJSONRenderer]
    def get_serializer_class(self):
         if self.request.method in ['GET']:
             return ChannelReadSerializer
         return ChannelSerializer

class OrganizerView(viewsets.ModelViewSet):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer
    filterset_class = OrganizerFilter
    renderer_classes = [CustomJSONRenderer]
    def get_serializer_class(self):
         if self.request.method in ['GET']:
             return OrganizerReadSerializer
         return OrganizerSerializer

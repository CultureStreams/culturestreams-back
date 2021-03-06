from rest_framework import viewsets
from django_filters import rest_framework as filters
from backend.models import Category, Event, Channel, Organizer, Associate
from .serializers import EventSerializer, ChannelSerializer, CategorySerializer, OrganizerSerializer, TagSerializer, AssociateSerializer
from .serializers import EventPostSerializer, ChannelPostSerializer, OrganizerPostSerializer, AssociatePostSerializer
from .filters import EventFilter, ChannelFilter, OrganizerFilter, CategoryFilter, TagFilter, AssociateFilter
from .renderers import CustomJSONRenderer
from taggit.models import Tag
from backend.pagination import EventPagination, OrganizerPagination

from rest_framework.response import Response
from rest_framework import status

# class CustomSearchFilter(filters.SearchFilter):
#     def get_search_fields(self, view, request):
#         if request.query_params.get('search_'):
#             return ['title']
#         return super(CustomSearchFilter, self).get_search_fields(view, request)

class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagSerializer
    filterset_class = TagFilter
    renderer_classes = [CustomJSONRenderer]

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter
    renderer_classes = [CustomJSONRenderer]

class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('start')
    serializer_class = EventSerializer
    filterset_class = EventFilter
    search_fields = ['name', 'subtitle', 'tags', 'description']
    # pagination_class = EventPagination
    renderer_classes = [CustomJSONRenderer]
    def get_serializer_class(self):
         if self.request.method in ['GET']:
             return EventSerializer
         return EventPostSerializer

class ChannelView(viewsets.ModelViewSet):
    queryset = Channel.objects.all().order_by('name')
    serializer_class = ChannelSerializer
    filterset_class = ChannelFilter
    renderer_classes = [CustomJSONRenderer]
    def get_serializer_class(self):
         if self.request.method in ['GET']:
             return ChannelSerializer
         return ChannelPostSerializer

class OrganizerView(viewsets.ModelViewSet):
    queryset = Organizer.objects.all().order_by('name')
    serializer_class = OrganizerSerializer
    filterset_class = OrganizerFilter
    # pagination_class = OrganizerPagination
    renderer_classes = [CustomJSONRenderer]
    def get_serializer_class(self):
         if self.request.method in ['GET']:
             return OrganizerSerializer
         return OrganizerPostSerializer

class AssociateView(viewsets.ModelViewSet):
    queryset = Associate.objects.all().order_by('name')
    serializer_class = AssociateSerializer
    filterset_class = AssociateFilter
    renderer_classes = [CustomJSONRenderer]
    def get_serializer_class(self):
         if self.request.method in ['GET']:
             return AssociateSerializer
         return AssociatePostSerializer

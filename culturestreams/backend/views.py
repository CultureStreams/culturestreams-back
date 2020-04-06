from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import Category, Event, Plattform, Organizer
from taggit.models import Tag
from .serializers import EventSerializer, PlattformSerializer, CategorySerializer, OrganizerSerializer, TagSerializer

class TagsFilter(filters.CharFilter):
    def filter(self, qs, value):
        if value:
            tags = [tag.strip() for tag in value.split(',')]
            qs = qs.filter(tags__name__in=tags).distinct()
        return qs

class EventFilter(filters.FilterSet):
    start = filters.DateTimeFromToRangeFilter()
    end = filters.DateTimeFromToRangeFilter()
    tags = TagsFilter(field_name='tags')
    class Meta:
        model = Event
        fields = ('id','name','category','organizer','slug','start','end','freeOfCharge','availableLiveOnly')

class PlattformFilter(filters.FilterSet):
    tags = TagsFilter(field_name='tags')
    class Meta:
        model = Plattform
        fields = ('id','category','organizer','slug','freeOfCharge','availableLiveOnly')

class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_fields = ('id','name','slug')

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_fields = ('id','name','slug')

class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_class = EventFilter

class PlattformView(viewsets.ModelViewSet):
    queryset = Plattform.objects.all()
    serializer_class = PlattformSerializer
    filterset_class = PlattformFilter

class OrganizerView(viewsets.ModelViewSet):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer
    filter_fields = ('id','name','category','slug')

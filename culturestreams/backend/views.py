from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework as filters
from django.db import models
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
    dateFrom = filters.DateTimeFilter(field_name='start', lookup_expr='gte')
    dateTo = filters.DateTimeFilter(field_name='start', lookup_expr='lt')
    tags = TagsFilter(field_name='tags')
    class Meta:
        Model = Event
        fields = ('dateFrom','dateTo','tags')

class PlattformFilter(filters.FilterSet):
    tags = TagsFilter(field_name='tags')
    class Meta:
        Model = Plattform
        fields = ('tags',)

class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_fields = ('id','name','slug')
    # permission_classes = (IsAuthenticatedOrReadOnly,)

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_fields = ('id',)
    # permission_classes = (IsAuthenticatedOrReadOnly,)

class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_fields = ('id','name','category','organizer','freeOfCharge','availableLiveOnly', 'datePublished')
    filterset_class = EventFilter
    #permission_classes = (IsAuthenticatedOrReadOnly,)

class PlattformView(viewsets.ModelViewSet):
    queryset = Plattform.objects.all()
    serializer_class = PlattformSerializer
    filter_fields = ('id','category','organizer','freeOfCharge','availableLiveOnly')
    filterset_class = EventFilter
    # permission_classes = (IsAuthenticatedOrReadOnly,)

class OrganizerView(viewsets.ModelViewSet):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer
    filter_fields = ('id','name','category')
    #permission_classes = (IsAuthenticatedOrReadOnly,)

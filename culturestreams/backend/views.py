from django.shortcuts import render
from rest_framework import viewsets
from .models import Event, Plattform, Category, Tag
from .serializers import EventSerializer, PlattformSerializer, CategorySerializer, TagSerializer

class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_fields = ('id', 'start','category','organizer')

class PlattformView(viewsets.ModelViewSet):
    queryset = Plattform.objects.all()
    serializer_class = PlattformSerializer
    filter_fields = ('id', 'category',)

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_fields = ('id',)

class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_fields = ('id',)

from django.shortcuts import render
from rest_framework import viewsets
from .models import Event, Plattform, Category, Tag
from .serializers import EventSerializer, PlattformSerializer, CategorySerializer, TagSerializer

class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_fields = ('startDate','category','organizer')

class PlattformView(viewsets.ModelViewSet):
    queryset = Plattform.objects.all()
    serializer_class = PlattformSerializer
    filter_fields = ('category',)

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

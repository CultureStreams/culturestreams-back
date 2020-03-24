from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Tag, Category, SubCategory, Event, Plattform, Organizer
from .serializers import EventSerializer, PlattformSerializer, CategorySerializer, TagSerializer, SubCategorySerializer, OrganizerSerializer

class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_fields = ('id',)
    permission_classes = (IsAuthenticatedOrReadOnly,)

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_fields = ('id',)
    permission_classes = (IsAuthenticatedOrReadOnly,)

class SubCategoryView(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    filter_fields = ('id',)
    permission_classes = (IsAuthenticatedOrReadOnly,)

class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_fields = ('id','name','start','category','organizer','freeOfCharge','availableLiveOnly','tags')
    #permission_classes = (IsAuthenticatedOrReadOnly,)

class PlattformView(viewsets.ModelViewSet):
    queryset = Plattform.objects.all()
    serializer_class = PlattformSerializer
    filter_fields = ('id','category','organizer','freeOfCharge','availableLiveOnly','tags')
    permission_classes = (IsAuthenticatedOrReadOnly,)

class OrganizerView(viewsets.ModelViewSet):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer
    filter_fields = ('id','name','category','tags')
    #permission_classes = (IsAuthenticatedOrReadOnly,)

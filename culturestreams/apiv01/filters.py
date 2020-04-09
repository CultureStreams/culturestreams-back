from rest_framework import viewsets
from django.db import models
from django_filters import rest_framework as filters
from backend.models import Category, Event, Channel, Organizer
from taggit.models import Tag
from .serializers import EventSerializer, ChannelSerializer, CategorySerializer, OrganizerSerializer, TagSerializer

class TagFilter(filters.FilterSet):
    class Meta:
        model = Tag
        fields = ('id','name','slug')

class TagsFilter(filters.CharFilter):
    def filter(self, qs, value):
        if value:
            tags = [tag.strip() for tag in value.split(',')]
            qs = qs.filter(tags__name__in=tags).distinct()
        return qs

class CategoryFilter(filters.FilterSet):
    class Meta:
        model = Category
        fields = ('id','name','slug')

class OrganizerFilter(filters.FilterSet):
    tags = TagsFilter(field_name='tags')
    category_name = filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        field_name="category__name",
        to_field_name="name",
    )
    category_id = filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        field_name="category__id",
        to_field_name="id",
    )
    category_slug = filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        field_name="category__slug",
        to_field_name="slug",
    )
    class Meta:
        model = Organizer
        fields = ('id','name','category','slug')

class ChannelFilter(filters.FilterSet):
    tags = TagsFilter(field_name='tags')
    category_name = filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        field_name="category__name",
        to_field_name="name",
    )
    category_id = filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        field_name="category__id",
        to_field_name="id",
    )
    category_slug = filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        field_name="category__slug",
        to_field_name="slug",
    )
    organizer_id = filters.ModelMultipleChoiceFilter(
        queryset=Organizer.objects.all(),
        field_name="organizer__id",
        to_field_name="id",
    )
    organizer_name = filters.ModelMultipleChoiceFilter(
        queryset=Organizer.objects.all(),
        field_name="organizer__name",
        to_field_name="name",
    )
    organizer_slug = filters.ModelMultipleChoiceFilter(
        queryset=Organizer.objects.all(),
        field_name="organizer__slug",
        to_field_name="slug",
    )
    class Meta:
        model = Channel
        fields = ('id','category','organizer','slug','freeOfCharge','availableLiveOnly')

class EventFilter(filters.FilterSet):
    start = filters.DateTimeFromToRangeFilter()
    end = filters.DateTimeFromToRangeFilter()
    tags = TagsFilter(field_name='tags')
    category_name = filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        field_name="category__name",
        to_field_name="name",
    )
    category_id = filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        field_name="category__id",
        to_field_name="id",
    )
    category_slug = filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        field_name="category__slug",
        to_field_name="slug",
    )
    organizer_id = filters.ModelMultipleChoiceFilter(
        queryset=Organizer.objects.all(),
        field_name="organizer__id",
        to_field_name="id",
    )
    organizer_name = filters.ModelMultipleChoiceFilter(
        queryset=Organizer.objects.all(),
        field_name="organizer__name",
        to_field_name="name",
    )
    organizer_slug = filters.ModelMultipleChoiceFilter(
        queryset=Organizer.objects.all(),
        field_name="organizer__slug",
        to_field_name="slug",
    )
    class Meta:
        model = Event
        fields = ('id','name','category','organizer','slug','start','end','freeOfCharge','availableLiveOnly')

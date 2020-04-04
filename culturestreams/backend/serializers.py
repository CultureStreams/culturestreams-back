from rest_framework import serializers
from .models import Category, Event, Plattform, Organizer
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
from taggit.models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','name','slug')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = ('__all__')

class EventSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Event
        fields = ('__all__')
    #def to_representation(self, instance):
        #rep_cat = super(EventSerializer, self).to_representation(instance)
        #rep_cat['category'] = instance.category.name
        #return rep_cat

class PlattformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plattform
        fields = ('__all__')
    #def to_representation(self, instance):
        #rep_cat = super(PlattformSerializer, self).to_representation(instance)
        #rep_cat['category'] = instance.category.name
        #return rep_cat

from rest_framework import serializers
from backend.models import Category, Event, Channel, Organizer
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
from taggit.models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        resource_name = 'tags'
        fields = ('id','name','slug')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        resource_name = 'categories'
        fields = ('__all__')

class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        resource_name = 'organizers'
        fields = ('__all__')

class EventSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Event
        resource_name = 'events'
        fields = ('__all__')
    #def to_representation(self, instance):
        #rep_cat = super(EventSerializer, self).to_representation(instance)
        #rep_cat['category'] = instance.category.name
        #return rep_cat

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        resource_name = 'channels'
        fields = ('__all__')
    #def to_representation(self, instance):
        #rep_cat = super(ChannelSerializer, self).to_representation(instance)
        #rep_cat['category'] = instance.category.name
        #return rep_cat

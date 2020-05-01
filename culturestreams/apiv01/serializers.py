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
        read_only_fields = ['categories']

class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        resource_name = 'organizer'
        fields = ('__all__')

class OrganizerReadSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    category = CategorySerializer(many=False, read_only=True)
    class Meta:
        model = Organizer
        resource_name = 'organizers'
        fields = ('__all__')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        resource_name = 'event'
        fields = ('__all__')

class EventReadSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    category = CategorySerializer(many=False, read_only=True)
    organizer = OrganizerSerializer(many=False)
    class Meta:
        model = Event
        resource_name = 'events'
        fields = ('__all__')
        # read_only_fields = ['organizers', 'categories', 'tags']

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        resource_name = 'channel'
        fields = ('__all__')

class ChannelReadSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    category = CategorySerializer(many=False, read_only=True)
    organizer = OrganizerSerializer(many=False)
    class Meta:
        model = Channel
        resource_name = 'channels'
        fields = ('__all__')

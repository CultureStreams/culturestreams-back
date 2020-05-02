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

class OrganizerNestedSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    # category = CategorySerializer(many=False, read_only=True)
    class Meta:
        model = Organizer
        resource_name = 'organizers'
        fields = ('__all__')
    def to_representation(self, instance):
        data = super(OrganizerNestedSerializer, self).to_representation(instance)
        data['category'] = CategorySerializer(instance=instance.category).data
        return data

class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        resource_name = 'organizer'
        fields = ('__all__')

class EventNestedSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    # categoryId = serializers.IntegerField(source='category')
    # organizerId = serializers.IntegerField(source='organizer')
    class Meta:
        model = Event
        resource_name = 'event'
        fields = ('__all__')
    def to_representation(self, instance):
        data = super(EventNestedSerializer, self).to_representation(instance)
        data['organizer'] = OrganizerSerializer(instance=instance.organizer).data
        data['category'] = CategorySerializer(instance=instance.category).data
        return data

class EventSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Event
        resource_name = 'events'
        fields = ('__all__')

class ChannelNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        resource_name = 'channel'
        fields = ('__all__')
    def to_representation(self, instance):
        data = super(ChannelNestedSerializer, self).to_representation(instance)
        data['organizer'] = OrganizerSerializer(instance=instance.organizer).data
        data['category'] = CategorySerializer(instance=instance.category).data
        return data

class ChannelSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Channel
        resource_name = 'channels'
        fields = ('__all__')

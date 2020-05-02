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

class OrganizerSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Organizer
        resource_name = 'organizers'
        fields = ('__all__')
    def to_representation(self, instance):
        data = super(OrganizerSerializer, self).to_representation(instance)
        data['category'] = CategorySerializer(instance=instance.category).data
        return data

class OrganizerPostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    categoryId = serializers.IntegerField(source='category_id')
    class Meta:
        model = Organizer
        resource_name = 'organizer'
        fields = ('__all__')
    def to_representation(self, instance):
        data = super(OrganizerPostSerializer, self).to_representation(instance)
        data['category'] = CategorySerializer(instance=instance.category).data
        return data

class OrganizerBasicSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Organizer
        resource_name = 'organizer'
        fields = ('__all__')

class EventSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Event
        resource_name = 'events'
        fields = ('__all__')
    def to_representation(self, instance):
        data = super(EventSerializer, self).to_representation(instance)
        data['organizer'] = OrganizerBasicSerializer(instance=instance.organizer).data
        data['category'] = CategorySerializer(instance=instance.category).data
        return data

class EventPostSerializer(TaggitSerializer, serializers.ModelSerializer):
    categoryId = serializers.IntegerField(source='category_id')
    organizerId = serializers.IntegerField(source='organizer_id')
    tags = TagListSerializerField()
    class Meta:
        model = Event
        resource_name = 'event'
        fields = ('__all__')
    def to_representation(self, instance):
        data = super(EventPostSerializer, self).to_representation(instance)
        data['organizer'] = OrganizerBasicSerializer(instance=instance.organizer).data
        data['category'] = CategorySerializer(instance=instance.category).data
        return data

class ChannelSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Channel
        resource_name = 'channels'
        fields = ('__all__')
    def to_representation(self, instance):
        data = super(ChannelSerializer, self).to_representation(instance)
        data['organizer'] = OrganizerBasicSerializer(instance=instance.organizer).data
        data['category'] = CategorySerializer(instance=instance.category).data
        return data

class ChannelPostSerializer(TaggitSerializer, serializers.ModelSerializer):
    categoryId = serializers.IntegerField(source='category_id')
    organizerId = serializers.IntegerField(source='organizer_id')
    tags = TagListSerializerField()
    class Meta:
        model = Channel
        resource_name = 'channel'
        fields = ('__all__')
    def to_representation(self, instance):
        data = super(ChannelPostSerializer, self).to_representation(instance)
        data['organizer'] = OrganizerBasicSerializer(instance=instance.organizer).data
        data['category'] = CategorySerializer(instance=instance.category).data
        return data

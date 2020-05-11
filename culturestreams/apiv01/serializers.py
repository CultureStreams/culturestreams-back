from rest_framework import serializers
from backend.models import Category, Event, Channel, Organizer, Associate
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

class AssociateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        resource_name = 'organizers'
        fields = ('__all__')

class AssociatePostSerializer(serializers.ModelSerializer):
    # associateId = serializers.IntegerField(source='associate_id')
    class Meta:
        model = Associate
        resource_name = 'associate'
        fields = ('__all__')
    # def to_representation(self, instance):
    #     data = super(AssociatePostSerializer, self).to_representation(instance)
    #     data['associate'] = AssociateSerializer(instance=instance.associate).data
    #     return data

class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        resource_name = 'organizers'
        fields = ('__all__')

class OrganizerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        resource_name = 'organizer'
        fields = ('__all__')

class EventSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    category = CategorySerializer(many=False, read_only=True)
    organizer = OrganizerSerializer(many=False)
    associates = AssociateSerializer(many=True)
    class Meta:
        model = Event
        resource_name = 'events'
        fields = ('__all__')

class EventPostSerializer(TaggitSerializer, serializers.ModelSerializer):
    categoryId = serializers.IntegerField(source='category_id')
    organizerId = serializers.IntegerField(source='organizer_id')
    # associates = serializers.IntegerField(source='associate_id')
    tags = TagListSerializerField()
    class Meta:
        model = Event
        resource_name = 'event'
        fields = ('__all__')
    def to_representation(self, instance):
        data = super(EventPostSerializer, self).to_representation(instance)
        data['organizer'] = OrganizerSerializer(instance=instance.organizer).data
        data['category'] = CategorySerializer(instance=instance.category).data
        # data['associates'] = AssociateSerializer(instance=instance.associate).data
        return data

class ChannelSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    category = CategorySerializer(many=False, read_only=True)
    organizer = OrganizerSerializer(many=False)
    class Meta:
        model = Channel
        resource_name = 'channels'
        fields = ('__all__')

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
        data['organizer'] = OrganizerSerializer(instance=instance.organizer).data
        data['category'] = CategorySerializer(instance=instance.category).data
        return data

from rest_framework import serializers
from .models import Tag, Category, SubCategory, Event, Plattform, Organizer

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('__all__')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('__all__')

class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = ('__all__')

class EventSerializer(serializers.ModelSerializer):
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

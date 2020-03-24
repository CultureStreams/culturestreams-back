from rest_framework import serializers
from .models import Event, Tag, Plattform, Category

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'parent')

# Serializers define the API representation.
class EventSerializer(serializers.ModelSerializer):
    #tags = TagSerializer(many=True, read_only=True)
    #dates = serializers.SerializerMethodField('get_dates')

    class Meta:
        model = Event
        fields = ('__all__')
        #fields = '__all__'
    def to_representation(self, instance):
        rep_cat = super(EventSerializer, self).to_representation(instance)
        rep_cat['category'] = instance.category.name
        return rep_cat

class PlattformSerializer(serializers.ModelSerializer):
    #tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Plattform
        fields = ('__all__')
        #fields = '__all__'
    def to_representation(self, instance):
        rep_cat = super(PlattformSerializer, self).to_representation(instance)
        rep_cat['category'] = instance.category.name
        return rep_cat

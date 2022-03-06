"""
Book: Building RESTful Python Web Services
"""
from rest_framework import serializers
from dogs.models import Dog
from dogs.models import Breed


class DogSerializer(serializers.HyperlinkedModelSerializer):
    # We want to display the breed named, not the id number
    breed = serializers.SlugRelatedField(queryset=Breed.objects.all(), slug_field='name')
    class Meta:
        model = Dog
        fields = (
            'id',
            'name',
            'age',
            'breed',
            'gender',
            'color',
            'favoritefood',
            'favoritetoy'
            )
            
class BreedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Breed
        fields = (
            'id',
            'name',
            'size',
            'friendliness',
            'trainability',
            'sheddingamount',
            'exerciseneeds',
            ) 
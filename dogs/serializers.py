"""
Book: Building RESTful Python Web Services
"""
from rest_framework import serializers
from dogs.models import Dog
from dogs.models import Breed

class BreedSerializer(serializers.HyperlinkedModelSerializer):
    
    games = serializers.HyperlinkedRelatedField(
    #HyperlinkedRelatedField with many and read_only equal to True because it is a one-to-many relationship and it is read-only
        many=True,
        read_only=True,
        view_name='game-detail')
    # A Meta inner class that declares two attributes: model and fields.
    class Meta:
        model = GameCategory  #The model attribute specifies the model related to the serializer, that is, the GameCategory class
        # The fields attribute specifies a tuple of string whose values indicates the field names that we want 
        # to include in the serialization from the related model. We also specified pk and url as members of tuple
        fields = (
            'url',
            'pk',
            'name',
            'games') 


class DogSerializer(serializers.HyperlinkedModelSerializer):
    # We want to display the game cagory's name instead of the id
    dog = serializers.SlugRelatedField(queryset=Dog.objects.all(), slug_field='name')

    class Meta:
        model = Dog
        fields = (
            'url',
            'game_category',
            'name',
            'release_date',
            'played')

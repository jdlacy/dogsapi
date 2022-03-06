from rest_framework.response import Response
from dogs.models import Dog, Breed
from dogs.serializers import DogSerializer, BreedSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
# Dog List View
class DogList(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    name = "Different Dogs"

# Dog Detail View
class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    name = "Dog Details"

# Breed List View
class BreedList(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    name = 'Breeds'

# Breed Detail View 
class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    name = "Breed Details"

class ApiRoot(generics.GenericAPIView):
    name = 'The Dogs API'
    def get(self, request, *args, **kwargs):
        return Response({
            'Different Dogs': reverse(DogList.name, request=request),
            'Breeds': reverse(BreedList.name, request=request),
            'Dog Details': reverse(DogDetail.name, request=request),
            'Breed Details': reverse(BreedDetail.name, request=request)
            })

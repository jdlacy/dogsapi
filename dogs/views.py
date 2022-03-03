from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from dogs.models import Dog
from dogs.models import Breed
from dogs.serializers import DogSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

# Dog Detail View
@csrf_exempt
def dog_detail(request, pk):
    try:
        dog = Dog.objects.get(pk=pk)
    except Dog.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        dog_serializer = DogSerializer(dog)
        return JSONResponse(dog_serializer.data)

    elif request.method == 'PUT':
        dog_data = JSONParser().parse(request)
        dog_serializer = DogSerializer(dog, data=dog_data)
        if dog_serializer.is_valid():
            dog_serializer.save()
            return JSONResponse(dog_serializer.data)
        return JSONResponse(dog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        dog.delete()  
        return Response(status=status.HTTP_204_NO_CONTENT)

# Dog List View
@csrf_exempt
def dog_list(request):
    if request.method == 'GET':
        dogs = Dog.objects.all()
        dogs_serializer = DogSerializer(dogs, many=True)
        return JSONResponse(dogs_serializer.data)

    elif request.method == 'POST':
        dog_data = JSONParser().parse(request)
        dog_serializer = DogSerializer(data=dog_data)
        if dog_serializer.is_valid():
            dog_serializer.save()
            return JSONResponse(dog_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(dog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Breed Detail View
@csrf_exempt
def breed_detail(request, pk):
    try:
        breed = Breed.objects.get(pk=pk)
    except Breed.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        dog_serializer = DogSerializer(dog)
        return JSONResponse(dog_serializer.data)

    elif request.method == 'PUT':
        dog_data = JSONParser().parse(request)
        dog_serializer = DogSerializer(dog, data=dog_data)
        if dog_serializer.is_valid():
            dog_serializer.save()
            return JSONResponse(dog_serializer.data)
        return JSONResponse(dog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        dog.delete()  
        return Response(status=status.HTTP_204_NO_CONTENT)

# Breed List View
@csrf_exempt
def dog_list(request):
    if request.method == 'GET':
        dogs = Dog.objects.all()
        dogs_serializer = DogSerializer(dogs, many=True)
        return JSONResponse(dogs_serializer.data)

    elif request.method == 'POST':
        dog_data = JSONParser().parse(request)
        dog_serializer = DogSerializer(data=dog_data)
        if dog_serializer.is_valid():
            dog_serializer.save()
            return JSONResponse(dog_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(dog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
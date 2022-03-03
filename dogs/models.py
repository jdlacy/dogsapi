from statistics import mode
from tkinter import CASCADE
from turtle import color
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Dog Model
class Dog(models.Model):
    name = models.CharField(max_length=200) # name (a character string)
    age = models.IntegerField() # age (an integer)
    breed = models.ForeignKey( # breed (a foreign key to the Breed Model)
        'Breed',
        related_name='dogs',
        on_delete=models.CASCADE)
    gender = models.CharField(max_length=200) # gender (a character string)
    color = models.CharField(max_length=200)      # color (a character string)
    favoritefood = models.CharField(max_length=200) # favoritefood (a character string)
    favoritetoy = models.CharField(max_length=200) # favoritetoy (a character string)
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

# Breed Model
class Breed(models.Model):
    #Options
    SIZE_CHOICES = (
        ('TINY', 'Tiny'),
        ('SMALL', 'Small'),
        ('MEDIUM', 'Medium'),
        ('LARGE', 'Large'),
    )

    name = models.CharField(max_length=200) # name (a character string)

    size = models.CharField( # size (a character string) [should accept Tiny, Small, Medium, Large]
        max_length=200, 
        choices=SIZE_CHOICES,
        default='MEDIUM',
    )

    friendliness = models.IntegerField( # friendliness (an integer field) [should accept values from 1-5]
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    trainability = models.IntegerField( # trainability (an integer field) [should accept values from 1-5]
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    sheddingamount = models.IntegerField( # sheddingamount (an integer field) [should accept values from 1-5]
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    exerciseneeds = models.IntegerField( # exerciseneeds (an integer field) [should accept values from 1-5]
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
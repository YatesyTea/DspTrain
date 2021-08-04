from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    calories = models.IntegerField
    fat = models.IntegerField
    protein = models.IntegerField
    sodium = models.IntegerField
    ingredients = models.CharField
    directions = models.CharField
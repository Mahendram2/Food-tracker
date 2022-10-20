from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models

# Create your models here.
class Food(models.Model):
    name=models.CharField(max_length=100, blank=True, null=True)
    calories=models.FloatField(blank=True, null=True)
    carbohydrates=models.FloatField(blank=True, null=True)
    protein=models.FloatField(blank=True, null=True)
    fat=models.FloatField(blank=True, null=True)
    fiber=models.FloatField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('foods_detail', args = [str(self.id)])
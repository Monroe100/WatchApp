from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length =30)
    neighbourhood_location = models.CharField(max_length = 30)
    occupants_count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


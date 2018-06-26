from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length =30)
    neighbourhood_location = models.CharField(max_length = 30)
    occupants_count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.neighbourhood_name

    def create_neighbourhood(self):
        '''Method to create a neighbourhood'''
        self.create()

    def delete_neighbourhood(self):
        '''Method to delete a neighbourhood'''
        self.delete()

    @classmethod
    def get_neighbourhoods(cls):
        '''
        Method that gets all image posts from the database
        Returns:
            get_posts : list of image post objects from the database
        ''' 
        Neighbourhoods = cls.objects.all()
        return Neighbourhoods


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





class Profile(models.Model):
    name = models.CharField(max_length =20)
    neighbourhood = models.ForeignKey('Neighbourhood')
    email = models.CharField(max_length = 30)
    profile_pic = models.ImageField(upload_to='occupants/')
    occupant_id = models.IntegerField(unique = True)
    location = models.CharField(max_length= 30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile_name

    def create_Profile(self):
        '''Method to create a profile'''
        self.create()

    def delete_profile(self):
        '''Method to delete a profile'''
        self.delete()

    @classmethod
    def get_profile(cls):
       
        Profiles = cls.objects.all()
        return Profiles

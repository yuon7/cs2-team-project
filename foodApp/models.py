# foodApp/models.py
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    cuisine_type = models.CharField(max_length=50)
    price_range = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
#class UploadImage(models.Model):
   # image = models.ImageField(uplosd_to='img/')


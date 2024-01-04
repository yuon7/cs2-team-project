from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)  
    price_range = models.CharField(max_length=50)
    like=models.IntegerField(default=0)

    def __str__(self):
        return self.name

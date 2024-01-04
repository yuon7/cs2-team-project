from django.db import models
from django.utils import timezone


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    price_range = models.CharField(max_length=50)
    like = models.IntegerField(default=0)
    slug = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE)  # レストランへの外部キー
    title = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    posted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

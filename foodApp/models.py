from django.db import models
from django.utils import timezone

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)  
    price_range = models.CharField(max_length=50)
    like=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Comment(models. Model):
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    article = models.ForeignKey(Restaurant, related_name='comment', on_delete=models.CASCADE)

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)
    like = models.IntegerField(default=0)

    def publish(self):
        self.publish_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
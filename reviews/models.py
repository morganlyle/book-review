from django.db import models

# Create your models here.
class Review(models.Model):
    coverImage = models.URLField()
    title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    rating = models.SmallIntegerField()
    authors = models.CharField(max_length=100)
    summary = models.TextField()
    review = models.TextField()
    created = models.DateTimeField()

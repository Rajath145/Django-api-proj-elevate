from django.db import models

# Create your models here.
class movies(models.Model):
    title=models.CharField(max_length=100)
    cast=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    budget=models.IntegerField()
    collection=models.IntegerField()
    streaming=models.CharField(max_length=100)
    rating=models.IntegerField()
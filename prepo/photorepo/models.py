from django.db import models
from .storage import PhotoStorage
from django.urls import reverse

class Photo(models.Model):
    pid         = models.BigAutoField(primary_key=True)
    photoName   = models.CharField(max_length=500)
    # authorId    = models.ForeignKey('User', on_delete=models.CASCADE)
    # author      = models.CharField(max_length=500)
    tags        = models.CharField(max_length=1000)     #Will be stored as a string rep of JSON object
    date        = models.DateField(auto_now=True)
    image       = models.ImageField(storage=PhotoStorage())

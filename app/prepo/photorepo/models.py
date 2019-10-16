from django.db import models
from .storage import PhotoStorage
from django.urls import reverse

# Create your models here.
class Photo(models.Model):
    _id         = models.CharField(unique=True, max_length=500, primary_key=True)
    photoName   = models.CharField(max_length=500)
    # authorId    = models.ForeignKey('User', on_delete=models.CASCADE)
    # author      = models.CharField(max_length=500)
    tags        = models.CharField(max_length=1000, unique=True)
    date        = models.DateField(auto_now=True)
    # image       = models.ImageField(storage=PhotoStorage()) # TODO: firgure out how to add proper url field???
    image       = models.ImageField(upload_to='images/') 
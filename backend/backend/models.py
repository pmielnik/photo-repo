# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from djongo import models as dmodels
from django.contrib.postgres.fields import ArrayField

from rest_framework import serializers


from django.core.files.storage import Storage
from django.conf import settings
import gridfs
from base64 import b64decode
import backend.utils.database as db
from django.urls import reverse

class PhotoStorage(Storage):
    def __init__(self, filename=None, photoId=None):
        if filename is None:
            filename = settings.BASE_DIR
        self.filename = filename
        self.photoId = photoId
    
    def _open(self, _id):
        return db.database.findPhoto(_id)

    def _save(self, name, data):
        db.database.insertPhoto(data, self.filename, self.photoId)

    def exists(self, name):
        print(self.photoId)
        return db.database.findPhoto(self.photoId) is not None

    def url(self, name):
        return db.database.findPhoto(self.photoId)

class User(models.Model):
    _id         = models.BigAutoField(primary_key=True)
    username    = models.CharField(max_length=500)
    firstName   = models.CharField(max_length=500)
    lastName    = models.CharField(max_length=500)
    email       = models.EmailField()

    @property
    def full_name(self):
        return '%s %s' % (self.firstName, self.lastName)

class Photo(models.Model):
    _id         = models.CharField(unique=True, max_length=500, primary_key=True)
    photoName   = models.CharField(max_length=500)
    authorId    = models.ForeignKey('User', on_delete=models.CASCADE)
    author      = models.CharField(max_length=500)
    tags        = models.CharField(max_length=1000, serialize=False, unique=True)
    date        = models.DateField(auto_now=True)
    image       = models.ImageField(storage=PhotoStorage(photoName, _id)) # TODO: add a upload_to and a storage field

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('photoName', 'author', 'tags', 'image')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName', 'email')

# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core import serializers
from rest_framework import generics

JSONSerializer      = serializers.get_serializer('json')
JSONDeserializer    = serializers.get_deserializer('json')


def index(request):
    return HttpResponse("Hello, world. You're at the photos index.")

# def image(request): 
  
#     if request.method == 'POST': 
#         form = ImageForm(request.POST, request.FILES) 
  
#         if form.is_valid(): 
#             form.save() 
#             return redirect('success') 
#     else: 
#         form = ImageForm() 
#     return render(request, 'image_form.html', {'form' : form}) #TODO: may be able to delete this; handle in js?
  
def success(request): 
    return HttpResponse('successfuly uploaded') 

class PhotoListCreate(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


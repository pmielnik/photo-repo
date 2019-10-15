# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core import serializers
from .models import Photo
from .serializers import PhotoSerializer
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


# 
class PhotoListCreate(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
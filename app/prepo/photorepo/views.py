from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Photo
from .forms import PhotoForm

# Create your views here.
class LandingPage(ListView):
    model = Photo
    template_name = 'photoList.html'

    #TODO: implement a get() method!

class ImageUpload(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'photoUpload.html'
    success_url = reverse_lazy('landing')

    #TODO: implement a post() method!
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Photo
from .forms import PhotoForm
from django.shortcuts import redirect
from django.db import router

# Create your views here.
class LandingPage(ListView):
    model = Photo
    template_name = 'photoList.html'

    #TODO: implement a get() method!
    def get(self, request):
        return super(LandingPage, self).get(request)

class ImageUpload(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'photoUpload.html'
    success_url = reverse_lazy('landing')

    #TODO: implement a post() method!

class ImageDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('landing')
    template_name = 'photoDelete.html'

    def delete(self, request, *args, **kwargs):
        us = router.db_for_write(self.get_object().image)
        self.get_object().image.storage.delete(self.get_object().image.name)
        self.get_object().delete(using=us)
        return redirect(self.success_url)
    # slug_field = 'id'

    # def get_object(self):
    #     return self.queryset.get(id=self.kwargs['id'])
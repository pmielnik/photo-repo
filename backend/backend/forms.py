from django import forms 
from .models import Photo
  
class ImageForm(forms.ModelForm): 
  
    class Meta: 
        model = Photo 
        fields = ['photoName', 'authorId', 'author', 'tags', 'image'] 
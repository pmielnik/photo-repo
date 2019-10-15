from rest_framework import serializers
from .models import Photo, User

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('photoName', 'authorId', 'author', 'tags', 'image')
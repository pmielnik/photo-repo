from rest_framework import serializers
from .models import Photo, User

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('photoName', 'author', 'tags', 'image')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName', 'email')
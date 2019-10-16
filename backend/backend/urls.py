from django.conf.urls import url
from django.urls import path
from . import models

urlpatterns = [
    url(r'^$', models.index, name='index'),
    # url(r'upload/', views.image, name = 'image_upload'ea), 
    url(r'success/', models.success, name = 'success'),
    path('api/photos/', models.PhotoListCreate.as_view()),
    path('api/users/', models.UserListCreate.as_view())
]
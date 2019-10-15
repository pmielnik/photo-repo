from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'upload/', views.image, name = 'image_upload'ea), 
    url(r'success/', views.success, name = 'success'),
    path('api/photos/', views.PhotoListCreate.as_view() )
]
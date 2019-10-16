from django.urls import path
from .views import LandingPage, ImageUpload

urlpatterns = [
    path('', LandingPage.as_view(), name='landing'),
    path('upload/', ImageUpload.as_view(), name='upload')
]
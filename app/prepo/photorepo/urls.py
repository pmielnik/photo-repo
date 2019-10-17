from django.urls import path
from .views import LandingPage, ImageUpload, ImageDelete

urlpatterns = [
    path('', LandingPage.as_view(), name='landing'),
    path('upload/', ImageUpload.as_view(), name='upload'),
    path('delete/<slug:pk>/', ImageDelete.as_view(), name='delete')
]
from django.urls import path
from .views import LandingPage, ImageUpload, ImageDelete, SearchPage

urlpatterns = [
    path('', LandingPage.as_view(), name='landing'),
    path('upload/', ImageUpload.as_view(), name='upload'),
    path('delete/<slug:pk>/', ImageDelete.as_view(), name='delete'),
    path('search/<slug:search_term>/', SearchPage.as_view(), name='search')
]
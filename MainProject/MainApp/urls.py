from django.urls import path
from .views import sample_api_view

urlpatterns = [
    path('sample/', sample_api_view, name='sample_api'),
]
from django.urls import path
from . import file, views

urlpatterns = [
    path('api/upload/', file.as_view(), name='display-file'),
    path('venue_pdf', views.venue_pdf, name='venue_pdf'),
    
]

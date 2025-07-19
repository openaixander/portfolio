from django.urls import path
from . import views

app_name = 'myport'

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('about/', views.about, name='about'),
    # Add more URL patterns as needed
]
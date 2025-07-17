from django.urls import path

from . import views

app_name = 'myport'

urlpatterns = [
    path('', views.index, name='index'),
]
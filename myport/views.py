from django.shortcuts import render

from .models import Project

# Create your views here.

def index(request):
    return render(request, 'myport/homepage.html')

def projects(request):
    # Here you would typically fetch projects from the database
    # For now, we will just render the projects template
    projects = Project.objects.all().prefetch_related('technologies', 'images', 'features')
    context = {
     'projects': projects
    }
    return render(request, 'myport/projects.html', context)

def about(request):
    return render(request, 'myport/about_me.html')
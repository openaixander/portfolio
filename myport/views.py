from django.shortcuts import render

from .models import Project, DeveloperImage

# Create your views here.

def index(request):
    """Render the homepage."""
    # You can pass any context variables you need to the template here
    developer_image = DeveloperImage.objects.first()  # Assuming you have a single developer image
    
    context = {
        'developer_image': developer_image,
    }


    return render(request, 'myport/index.html', context)

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
from django.db import models

# Create your models here.

class Technology(models.Model):
    """Represents a technology used in projects."""
    name = models.CharField(max_length=100, unique=True)
    # description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"


class Project(models.Model):
    """Represents a project with its details."""
    title = models.CharField(max_length=200, help_text="Enter the project title")
    summary = models.TextField(help_text="Enter a brief summary of the project")
    live_link = models.URLField(blank=True, null=True, help_text="Enter the live link of the project")
    code_link = models.URLField(blank=True, null=True, help_text="Enter the code link of the project")
    
    technologies = models.ManyToManyField(Technology, related_name='projects', help_text="Select technologies used in the project")

    display_order = models.IntegerField(default=0, help_text="Order in which the project should be displayed")

    class Meta:
        ordering = ['display_order']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    """Represents an image associated with a project."""
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE, help_text="Select the project this image belongs to")
    image = models.ImageField(upload_to='projects/images/', help_text="Upload an image for the project")
    alt_text = models.CharField(max_length=200, blank=True, null=True, help_text="Enter a alt text for the image")

    class Meta:
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"

    def __str__(self):
        return f"{self.project.title} - {self.alt_text or 'Image'}"
        
class FeaturedProject(models.Model):
    """Represents a featured project."""
    project = models.ForeignKey(Project, related_name='features', on_delete=models.CASCADE, help_text="Select the project to feature")
    description = models.CharField(max_length=500, help_text="Enter a description for the featured project")

    class Meta:
        verbose_name = "Featured Project"
        verbose_name_plural = "Featured Projects"

    def __str__(self):
        return f"Featured: {self.description}"
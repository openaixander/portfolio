# myport/models.py
from django.db import models

class Technology(models.Model):
    """Represents a technology or tool, like 'Django' or 'Python'."""
    name = models.CharField(max_length=50, unique=True)
    # You could add an icon field here later if you want
    
    class Meta:
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name

class Project(models.Model):
    """Represents a single project in your portfolio."""
    title = models.CharField(max_length=100, help_text="The title of the project.")
    summary = models.TextField(help_text="A short summary of the project.")
    live_link = models.URLField(blank=True, null=True, help_text="The URL to the live demo.")
    code_link = models.URLField(blank=True, null=True, help_text="The URL to the source code on GitHub.")
    
    # Relationships
    technologies = models.ManyToManyField(Technology, related_name='projects', help_text="Select the technologies used for this project.")
    
    # For ordering projects on the page
    display_order = models.PositiveIntegerField(default=0, help_text="Projects with a lower number will appear first.")

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    """Represents a screenshot for a project's carousel."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_screenshots/', help_text="Upload a screenshot for the project.")
    alt_text = models.CharField(max_length=100, blank=True, help_text="Alt text for the image, for accessibility.")

    def __str__(self):
        return f"Image for {self.project.title}"

class Feature(models.Model):
    """Represents a single key feature of a project."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='features')
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description
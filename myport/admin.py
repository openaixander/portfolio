# myport/admin.py
from django.contrib import admin
from .models import Technology, Project, ProjectImage, Feature

# Allows you to add images and features directly when editing a project
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # How many extra empty image forms to show

class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 3 # Show 3 empty feature forms

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'live_link')
    list_filter = ('technologies',)
    search_fields = ('title', 'summary')
    inlines = [ProjectImageInline, FeatureInline]

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    search_fields = ('name',)
from django.contrib import admin
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    """
    Customizes the display of ContactSubmission model in the Django admin.
    """
    # Fields to display in the list view of the admin panel.
    list_display = ('name', 'email', 'created_at', 'is_read')
    
    # Fields that can be used to filter the submissions.
    list_filter = ('is_read', 'created_at')
    
    # Fields that can be searched.
    search_fields = ('name', 'email', 'message')
    
    # Makes the 'is_read' field editable directly from the list view.
    list_editable = ('is_read',)
    
    # By default, you can't edit non-editable fields.
    # We specify all fields to be visible in the detail view but not editable.
    readonly_fields = ('name', 'email', 'message', 'created_at')
from django.db import models

class ContactSubmission(models.Model):
    """
    Model to store messages submitted through the contact form.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    # This field automatically records when the message was sent.
    created_at = models.DateTimeField(auto_now_add=True)
    
    # A handy boolean field to track if you've read the message yet.
    is_read = models.BooleanField(default=False)

    class Meta:
        # This will ensure that in the admin panel, messages are ordered
        # from newest to oldest, which is most convenient.
        ordering = ['-created_at']
        
        # Sets a more readable name for the model in the admin interface.
        verbose_name = "Contact Submission"
         verbose_name_plural = "Contact Submissions"

    def __str__(self):
        # This is how each submission will be represented as a string,
        # for example, in the Django admin.
        return f"Message from {self.name} ({self.email})"
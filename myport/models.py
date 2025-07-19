from django.db import models

# Create your models here.

# Time to create the contadct form model
class ContactSubmission(models.Model):
    """Model to store contact form submissions."""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    # This field automatically records when the message was sent
    created_at = models.DateTimeField(auto_now_add=True)

    # A handy boolean field to track if the message has been read
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Submission"
        verbose_name_plural = "Contact Submissions"

    def __str__(self):
        return f"Message from {self.name} - {self.email}"

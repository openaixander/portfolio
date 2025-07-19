from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    """
    A form for users to submit contact messages, based on the ContactSubmission model.
    """
    class Meta:
        # Specifies the model this form is linked to.
        model = ContactSubmission
        
        # Lists the fields from the model to include in the form.
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        # This method allows us to customize the form fields after they are created.
        super().__init__(*args, **kwargs)
        
        # to match the styling of your original HTML template.
        # Here, we add CSS classes and placeholder text to each field's widget
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your Full Name',
            'required': True
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'your.email@example.com',
            'required': True
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your message here...',
            'rows': 5,
            'required': True
        })
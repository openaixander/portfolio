from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    """Form for submitting contact messages."""

    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'message']
        
    
    def __init__(self, *args, **kwargs):
        # This method allows us to customize the form fields after are created
        super().__init__(*args, **kwargs)
        
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
from django.shortcuts import render, redirect
from django.contrib import messages  # Import Django's messaging framework
from .forms import ContactForm

def contact_view(request):
    """
    Handles the display and processing of the contact form.
    """
    # Check if the request method is POST, which means the form has been submitted.
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request.
        form = ContactForm(request.POST)
        
        # Check if the form's data is valid according to the rules in our form class.
        if form.is_valid():
            # If the form is valid, save the new ContactSubmission object to the database.
            form.save()
            
            # Add a success message that will be displayed on the next page the user sees.
            # This is a much better user experience than a simple alert.
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            
            # Redirect the user back to the same contact page.
            # The page will now be clean, and the success message will appear.
            return redirect('contact') # Make sure you have a URL named 'contact'
        else:
            # If the form is not valid, add an error message.
            messages.error(request, 'There was an error in your form. Please check the fields and try again.')
    
    # If the request method is GET (i.e., the user is just visiting the page),
    # create a blank instance of the form.
    else:
        form = ContactForm()

    # Prepare the context dictionary to pass the form to the template.
    context = {
        'form': form
    }
    
    # Render the contact page template with the form.
    return render(request, 'contact/contact_me.html', context)
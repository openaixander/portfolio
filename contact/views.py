from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

def contact(request):
    """View to handle contact form submissions."""

    # checks whether the request method is POST
    if request.method == 'POST':
        # create a form instance with the submitted data
        form = ContactForm(request.POST)


        # checks if the form is valid
        if form.is_valid():
            # save the form data to the database
            form.save()
            # display a success message
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            # redirect to the same page or another page
            return redirect('contact:contact')

        else:
            # if the form is not valid, display an error message
            messages.error(request, 'There was an error sending your message. Please try again.')
    else:
        # if the request method is not POST, create an empty form
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'contact/contact_me.html', context)
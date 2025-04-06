from django.http import HttpRequest
from django.shortcuts import render, redirect
from .form import ContactForm

# Create your views here.

# This is the home page view function
def home_view(request):
    return render(request, 'form_app/home.html')

def contact_view(request: HttpRequest):
    if (request.method == 'POST'):
        form = ContactForm(request.POST)

        if form.is_valid():
            form.send_email()

            return redirect('contact-success')
    else:
        form = ContactForm()
    
    return render(request, 'form_app/contact.html', {
        'form': form
    })

def contact_success_view(request):
    return render(request, 'form_app/contact_success.html')
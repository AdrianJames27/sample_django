from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# For class-based views
from django.contrib.auth.mixins import LoginRequiredMixin
# For class-based views
from django.views import View
# Import the User class (model)
from django.contrib.auth.models import User
# Import the RegisterForm from forms.py
from .forms import RegisterForm

# Create your views here.
def register_view(request: HttpRequest):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=password)

            login(request, user)

            return redirect('home')
        else:
            return render(request, 'accounts/register.html', {
                'form': form
            })
    else:
        form = RegisterForm()

        return render(request, 'accounts/register.html', {
            'form': form
        })

def login_view(request: HttpRequest):
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            next_url = request.POST.get('next') or request.GET.get('next') or 'home'

            return redirect(next_url)
        else:
            error_message = 'Invalid Credentials!'
        
    return render(request, 'accounts/login.html', {
        'error': error_message
    })

def logout_view(request: HttpRequest):
    if request.method == 'POST':
        logout(request)

        return redirect('login')
    else:
        return render(request, 'accounts/logout.html')

# Home
# Using the decorator
@login_required
def home_view(request):
    return render(request, 'auth1_app/home.html')

# Protected View
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    # 'next' - to redirect URL
    redirect_field_name = 'redirect-to'

    def get(self, request):
        return render(request, 'registration/protected.html')
from django.shortcuts import render
from .models import Tour

# Create your views here.
def index(request):
    tours = Tour.objects.all()

    return render(request, 'tours/index.html', {
        'tours': tours
    })
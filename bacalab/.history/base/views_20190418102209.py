from django.shortcuts import render
from projects.models import Project

def home(request):
    context = {
        'projects' : Project.objects.all()
    }
    return render(request, 'base/home.html')
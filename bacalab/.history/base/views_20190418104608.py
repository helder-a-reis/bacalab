from django.shortcuts import render
from projects.models import Project

def home(request):
    context = {
        'projects' : Project.objects.get(projectKey="hipsterhood")
    }
    return render(request, 'base/home.html', context)
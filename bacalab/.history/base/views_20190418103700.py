from django.shortcuts import render
from projects.models import Project

def home(request):
    context = {
        #'projects' : Project.objects.all().filter(projectKey="hipsterhood")
        'project' : Project.objects.all().filter(projectKey="hipsterhood")
    }
    return render(request, 'base/home.html', context)
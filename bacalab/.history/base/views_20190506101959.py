from django.shortcuts import render
from projects.models import Project

def home(request):
    #TODO: get latest blog, 1 project and 1 music
    context = {
        #change this dictionary to choose which projects are in the showcase
        'project1' : Project.objects.get(projectKey="hipsterhood"),
        'project2' : Project.objects.get(projectKey="jsontranslator"),
    }
    return render(request, 'base/home.html', context)
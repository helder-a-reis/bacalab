from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project

class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'    

def jsontranslator(request):
    context = {
        'project' : Project.objects.get(projectKey="hipsterhood"),
    }
    return render(request, 'jsontranslator.html', context)
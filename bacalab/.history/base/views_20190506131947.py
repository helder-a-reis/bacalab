from django.shortcuts import render
from projects.models import Project
from blog.models import Post

def home(request):
    #TODO: get latest blog entry, 1 project and 1 music
    context = {
        #change this dictionary to choose which projects are in the showcase
        'highProject' : Project.objects.get(projectKey="jsontranslator"),
        'latestPost' : Post.objects.order_by('-date_posted')[0],
    }
    return render(request, 'base/home.html', context)
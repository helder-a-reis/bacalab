from django.shortcuts import render
from .models import Job

def profile(request):
    context = {
        'jobs': Job.objects.all()
    }
    return render(request, 'resume/profile.html')
from django.shortcuts import render
from .models import Job

def profile(request):
    context = {
        'jobs': Job.objects.all().order_by('-startYear')
    }
    return render(request, 'resume/profile.html', context)
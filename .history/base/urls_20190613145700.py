from django.urls import path, include

from . import views

urlpatterns = [
    #path('', views.home, name='base-home'),
    path('', include('resume.urls'), name='base-home'),
]
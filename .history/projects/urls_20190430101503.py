from django.urls import path
from .views import ProjectListView, ProjectDetailView
from . import views

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-home'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]
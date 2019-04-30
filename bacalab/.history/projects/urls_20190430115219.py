from django.urls import path
from .views import ProjectListView
from . import views

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects-home'),
    path('jsontranslator', views.jsontranslator, name='jsontranslator')
]
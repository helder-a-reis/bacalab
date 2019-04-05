from django.urls import path
from .views import PostListView
from . import views

urlpatters = [
    path('', PostListView.as_view(), name='blog-home')
]
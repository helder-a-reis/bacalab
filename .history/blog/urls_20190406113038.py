from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('profile/', views.profile, name='profile'),
]
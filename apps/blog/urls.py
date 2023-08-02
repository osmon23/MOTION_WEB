from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('reviews/', views.ReviewsListView.as_view(), name='reviews-list'),
    path('projects/', views.ProjectsListView.as_view(), name='projects')
]

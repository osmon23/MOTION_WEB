from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('reviews/', views.ReviewsListView.as_view(), name='reviews-list'),
    path('projects/', views.ProjectsListView.as_view(), name='projects'),
    path('news/', views.NewsListView.as_view(), name='news-list'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('best-articles/', views.BestArticlesListView.as_view(), name='best-list'),
    path('best-articles/<int:pk>/', views.BestArticlesDetailView.as_view(), name='best-detail'),
]

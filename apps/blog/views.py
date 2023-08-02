from rest_framework import generics
from .models import Post, Reviews, Projects
from .serializers import PostSerializer, ReviewsSerializer, ProjectsSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ReviewsListView(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


class ProjectsListView(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

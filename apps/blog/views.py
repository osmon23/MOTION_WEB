from rest_framework import generics
from .models import Post, Reviews, Projects, News, BestArticles, About, AboutUsGallery
from .serializers import PostSerializer, ReviewsSerializer, ProjectsSerializer, NewsSerializer, BestArticlesSerializer, \
    AboutSerializer, AboutUsGallerySerializer


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


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class BestArticlesListView(generics.ListAPIView):
    queryset = BestArticles.objects.all()
    serializer_class = BestArticlesSerializer


class BestArticlesDetailView(generics.RetrieveAPIView):
    queryset = BestArticles.objects.all()
    serializer_class = BestArticlesSerializer


class AboutView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AboutUsGalleryListView(generics.ListAPIView):
    queryset = AboutUsGallery.objects.all()
    serializer_class = AboutUsGallerySerializer

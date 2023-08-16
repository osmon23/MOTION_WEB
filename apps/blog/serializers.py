from rest_framework import serializers
from .models import Post, Tag, PostDescription, PostMedia, Reviews, Projects, News, BestArticles, About, AboutUsGallery


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class PostDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostDescription
        fields = ('description',)


class PostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = ('media',)


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    descriptions = PostDescriptionSerializer(many=True, read_only=True)
    media = PostMediaSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'created_at', 'tags', 'descriptions', 'media')


class NewsSerializer(PostSerializer):
    class Meta:
        model = News
        fields = ('id', 'news_title', 'news_created_at', 'tags', 'descriptions', 'media')


class BestArticlesSerializer(PostSerializer):
    class Meta:
        model = BestArticles
        fields = ('id', 'best_title', 'best_created_at', 'tags', 'descriptions', 'media')


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('id', 'file')


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'image', 'url')


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class AboutUsGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsGallery
        fields = ('id', 'image', 'file')
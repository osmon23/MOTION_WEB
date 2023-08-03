from rest_framework import serializers
from .models import Post, Tag, PostDescription, PostMedia, Reviews, Projects


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


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('id', 'file')


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'image', 'url')

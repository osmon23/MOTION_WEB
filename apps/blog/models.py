from django.db import models
from django.utils.translation import gettext_lazy as _

from .constants import TypeChoices


class Post(models.Model):
    title = models.CharField(
        _('title'),
        max_length=100,
    )
    created_at = models.DateTimeField(
        _('created at'),
        auto_now_add=True,
    )
    type = models.CharField(
        _('Type'),
        max_length=1,
        choices=TypeChoices.choices,
        default=TypeChoices.BLOG,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ['-created_at']


class Tag(models.Model):
    name = models.CharField(
        _('name'),
        max_length=50)
    posts = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='tags')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class PostDescription(models.Model):
    description = models.TextField(
        _('description'),
        max_length=1000)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='descriptions')

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = _('description')
        verbose_name_plural = _('descriptions')


class PostMedia(models.Model):
    media = models.FileField(
        _('media'),
        upload_to='post_media/')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='media')

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = _('media')
        verbose_name_plural = _('media')


class Reviews(models.Model):
    file = models.FileField(
        _('file'),
        upload_to='reviews/')


class Projects(models.Model):
    image = models.ImageField(
        _('Image'),
        upload_to='projects/'
    )
    url = models.URLField(
        _('URL'),
    )

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

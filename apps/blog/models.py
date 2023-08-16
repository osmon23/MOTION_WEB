from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=100,
    )
    created_at = models.DateTimeField(
        _('Created at'),
        auto_now_add=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ['-created_at']


class Tag(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=50,
    )
    posts = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='tags',
        verbose_name=_('Posts'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class PostDescription(models.Model):
    description = models.TextField(
        _('Description'),
        max_length=1000)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='descriptions',
        verbose_name=_('Post'),
    )

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = _('Description')
        verbose_name_plural = _('Descriptions')


class PostMedia(models.Model):
    media = models.FileField(
        _('Media'),
        upload_to='post_media/'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='media',
        verbose_name=_('Post'),
    )

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = _('Media')
        verbose_name_plural = _('Media')


class Reviews(models.Model):
    file = models.FileField(
        _('File'),
        upload_to='reviews/',
    )

    def __str__(self):
        return self
    
    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')


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


class News(Post):
    news_title = models.CharField(
        _('Title'),
        max_length=255,
    )
    news_created_at = models.DateTimeField(
        _('Created at'),
        auto_now_add=True,
    )

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')


class BestArticles(Post):
    best_title = models.CharField(
        _('Title'),
        max_length=255,
    )
    best_created_at = models.DateTimeField(
        _('Created at'),
        auto_now_add=True,
    )

    def __str__(self):
        return self.best_title

    class Meta:
        verbose_name = _('Best Article')
        verbose_name_plural = _('Best Articles')


class About(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=100,
    )
    description = models.TextField(
        _('Description'),
    )
    graduated = models.CharField(
        _('Graduated'),
        max_length=50,
    )
    years = models.CharField(
        _('Years'),
        max_length=50,
    )
    mentors = models.CharField(
        _('Mentors'),
        max_length=50,
    )
    work_offers = models.CharField(
        _('Work offers'),
        max_length=50,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('About')
        verbose_name_plural = _('About')


class AboutUsGallery(models.Model):
    image = models.ImageField(
        _('Image'),
        null=True,
        blank=True,
        upload_to='about_us/',
    )
    file = models.FileField(
        _('File'),
        null=True,
        blank=True,
        upload_to='about_us/'
    )

    def __str__(self):
        return self
    
    class Meta:
        verbose_name = _('About us gallery')
        verbose_name_plural = _('About us gallery')

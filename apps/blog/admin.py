from django.contrib import admin

from .models import Post, Tag, PostDescription, PostMedia, Reviews, Projects


class TagInline(admin.TabularInline):
    model = Tag
    extra = 1


class PostDescriptionInline(admin.TabularInline):
    model = PostDescription
    extra = 1


class PostMediaInline(admin.TabularInline):
    model = PostMedia
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        TagInline,
        PostDescriptionInline,
        PostMediaInline,
    ]
    save_on_top = True
    list_display = ('id', 'title', 'created_at', 'type')
    list_display_links = ('title',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'posts')
    list_display_links = ('name',)


@admin.register(PostDescription)
class PostDescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'post')
    list_display_links = ('description',)


@admin.register(PostMedia)
class PostMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'media', 'post')
    list_display_links = ('media',)


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'url')
    list_display_links = ('id', 'image', 'url')
    search_fields = ('id', 'image', 'utl')

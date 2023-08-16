from modeltranslation.translator import register, TranslationOptions

from .models import Post, Tag, PostDescription, About, News, BestArticles


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


@register(PostDescription)
class PostDescriptionTranslationOptions(TranslationOptions):
    fields = (
        'description',
    )


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
        'graduated',
        'years',
        'mentors',
        'work_offers',
    )


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = (
        'news_title',
    )


@register(BestArticles)
class BestArticlesTranslationOptions(TranslationOptions):
    fields = (
        'best_title',
    )

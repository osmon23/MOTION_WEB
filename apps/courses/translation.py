from modeltranslation.translator import register, TranslationOptions

from .models import Course, CoursesStack, Duration, Mentor, CourseFormat, TrialLesson, ForWho, WhatGive, Program


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'why_we',
        'description',
    )


@register(CoursesStack)
class CoursesStackTranslationOptions(TranslationOptions):
    fields = (
        'stack',
    )


@register(Duration)
class DurationTranslationOptions(TranslationOptions):
    fields = (
        'duration',
    )


@register(Mentor)
class MentorTranslationOptions(TranslationOptions):
    fields = (
        'first_name',
        'last_name',
        'description',
    )


@register(CourseFormat)
class CourseFormatTranslationOptions(TranslationOptions):
    fields = (
        'format',
        'description',
    )


@register(TrialLesson)
class TrialLessonTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'description',
    )


@register(ForWho)
class ForWhoTranslationOptions(TranslationOptions):
    fields = (
        'for_who',
    )


@register(WhatGive)
class WhatGiveTranslationOptions(TranslationOptions):
    fields = (
        'reason',
        'info',
    )


@register(Program)
class ProgramTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )

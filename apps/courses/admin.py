from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import Course, Duration, Mentor, CoursesImage, TrialLesson, CoursesStack, CourseFormat, ForWho, WhatGive, \
    Program


class CoursesStackInline(TranslationTabularInline):
    model = CoursesStack
    extra = 1


class CourseFormatInline(TranslationTabularInline):
    model = CourseFormat
    extra = 1


class CoursesImageInline(admin.TabularInline):
    model = CoursesImage
    extra = 1


class DurationInline(TranslationTabularInline):
    model = Duration
    extra = 1


class MentorInline(TranslationTabularInline):
    model = Mentor
    extra = 1


class ForWhoInline(TranslationTabularInline):
    model = ForWho
    extra = 1


class WhatGiveInline(TranslationTabularInline):
    model = WhatGive
    extra = 1


class ProgramInline(TranslationTabularInline):
    model = Program
    extra = 1


@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    inlines = [
        CoursesImageInline,
        DurationInline,
        MentorInline,
        CoursesStackInline,
        CourseFormatInline,
        ForWhoInline,
        WhatGiveInline,
        ProgramInline,
    ]
    save_on_top = True
    list_display = ('id', 'name', 'why_we', 'description')
    list_display_links = ('name',)


@admin.register(TrialLesson)
class TrialLessonAdmin(TranslationAdmin):
    save_on_top = True
    list_display = ('id', 'name', 'date', 'time', 'description')
    list_display_links = ('name',)


@admin.register(Mentor)
class MentorAdmin(TranslationAdmin):
    save_on_top = True
    list_display = ('id', 'first_name', 'last_name', 'description', 'photo')
    list_display_links = ('first_name', 'last_name')


@admin.register(Duration)
class DurationAdmin(TranslationAdmin):
    save_on_top = True
    list_display = ('id', 'duration',)


@admin.register(CoursesStack)
class CoursesStackAdmin(TranslationAdmin):
    list_display = ('id', 'stack',)
    list_display_links = ('stack',)


@admin.register(CourseFormat)
class CourseFormatAdmin(TranslationAdmin):
    list_display = ('id', 'format',)
    list_display_links = ('format',)


@admin.register(ForWho)
class ForWhoAdmin(TranslationAdmin):
    list_display = ('id', 'for_who',)
    list_display_links = ('for_who',)


@admin.register(WhatGive)
class WhatGiveAdmin(TranslationAdmin):
    list_display = ('id', 'reason', 'info')
    list_display_links = ('reason',)


@admin.register(Program)
class ProgramAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('title',)

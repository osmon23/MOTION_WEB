from django.contrib import admin

from .models import Course, Duration, Mentor, CoursesImage, TrialLesson, CoursesStack, CourseFormat, ForWho, WhatGive, \
    Program


class CoursesStackInline(admin.TabularInline):
    model = CoursesStack
    extra = 1


class CourseFormatInline(admin.TabularInline):
    model = CourseFormat
    extra = 1


class CoursesImageInline(admin.TabularInline):
    model = CoursesImage
    extra = 1


class DurationInline(admin.TabularInline):
    model = Duration
    extra = 1


class MentorInline(admin.TabularInline):
    model = Mentor
    extra = 1


class ForWhoInline(admin.TabularInline):
    model = ForWho
    extra = 1


class WhatGiveInline(admin.TabularInline):
    model = WhatGive
    extra = 1


class ProgramInline(admin.TabularInline):
    model = Program
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
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
class TrialLessonAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'name', 'date', 'time', 'description')
    list_display_links = ('name',)


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'first_name', 'last_name', 'description', 'photo')
    list_display_links = ('first_name', 'last_name')


@admin.register(Duration)
class DurationAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'duration',)


@admin.register(CoursesStack)
class CoursesStackAdmin(admin.ModelAdmin):
    list_display = ('id', 'stack',)
    list_display_links = ('stack',)


@admin.register(CourseFormat)
class CourseFormatAdmin(admin.ModelAdmin):
    list_display = ('id', 'format',)
    list_display_links = ('format',)


@admin.register(ForWho)
class ForWhoAdmin(admin.ModelAdmin):
    list_display = ('id', 'for_who',)
    list_display_links = ('for_who',)


@admin.register(WhatGive)
class WhatGiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'reason', 'info')
    list_display_links = ('reason',)


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('title',)

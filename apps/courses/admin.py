from django.contrib import admin

from .models import Course, Duration, Mentor, CoursesImage, TrialLesson, CoursesStack


class CoursesStackInline(admin.TabularInline):
    model = CoursesStack
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


@admin.register(Course)
class CorseAdmin(admin.ModelAdmin):
    inlines = [
        CoursesImageInline,
        DurationInline,
        MentorInline,
        CoursesStackInline,
    ]
    save_on_top = True
    list_display = ('name', 'why_we', 'description')
    list_display_links = ('name',)


@admin.register(TrialLesson)
class TrialLessonAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('name', 'date', 'time', 'description')
    list_display_links = ('name',)


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('first_name', 'last_name', 'description', 'photo')
    list_display_links = ('first_name', 'last_name')


@admin.register(Duration)
class DurationAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('duration',)


@admin.register(CoursesStack)
class CoursesStackAdmin(admin.ModelAdmin):
    list_display = ('stack',)
    list_display_links = ('stack',)

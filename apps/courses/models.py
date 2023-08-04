from django.db import models
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=100)
    why_we = models.TextField(
        _('Why we'),
        max_length=500,
    )
    description = models.TextField(
        _('Description'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')


class CoursesStack(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='courses_stacks',
    )
    stack = models.CharField(
        _('Stack'),
        max_length=100,
    )

    def __str__(self):
        return self.stack

    class Meta:
        verbose_name = _('Stack')
        verbose_name_plural = _('Stacks')


class Duration(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='durations',
    )
    duration = models.CharField(
        _('Duration'),
        max_length=50,
    )

    def __str__(self):
        return self.duration

    class Meta:
        verbose_name = _('Duration')
        verbose_name_plural = _('Durations')


class Mentor(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='mentors',
    )
    first_name = models.CharField(
        _('First name'),
        max_length=100,
    )
    last_name = models.CharField(
        _('Last name'),
        max_length=100,
    )
    description = models.TextField(
        _('Description'),
    )
    photo = models.ImageField(
        _('Photo'),
        upload_to='mentors/',
    )

    def __str__(self):
        return f' {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('Mentor')
        verbose_name_plural = _('Mentors')


class CourseFormat(models.Model):
    format = models.CharField(
        _('Format'),
        max_length=255,
    )
    description = models.TextField(
        _('Description'),
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='format',
    )

    def __str__(self):
        return self.format

    class Meta:
        verbose_name = _('Format')
        verbose_name_plural = _('Formats')


class CoursesImage(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='images',
    )
    image = models.ImageField(
        _('Image'),
        upload_to='courses/',
    )

    def __str__(self):
        return self.course.name

    class Meta:
        verbose_name = _('Course image')
        verbose_name_plural = _('Course images')


class TrialLesson(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=100,
    )
    date = models.DateField(
        _('Date'),
    )
    time = models.TimeField(
        _('Time'),
    )
    description = models.TextField(
        _('Description'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Trial lesson')
        verbose_name_plural = _('Trial lessons')


class ForWho(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='for_who',
    )
    for_who = models.TextField(
        _('For who'),
    )

    def __str__(self):
        return self.for_who

    class Meta:
        verbose_name = _('For who')
        verbose_name_plural = _('For who')


class WhatGive(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='what_give',
    )
    reason = models.CharField(
        _('What give'),
        max_length=100,
    )
    info = models.TextField(
        _('Info'),
    )

    def __str__(self):
        return self.reason

    class Meta:
        verbose_name = _('What give')
        verbose_name_plural = _('What give')


class Program(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='program',
    )
    title = models.CharField(
        _('title'),
        max_length=100,
    )
    description = models.TextField(
        _('Description'),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Program')
        verbose_name_plural = _('Program')
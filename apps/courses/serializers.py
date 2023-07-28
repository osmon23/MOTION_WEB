from rest_framework import serializers
from .models import Course, Duration, Mentor, CoursesImage, TrialLesson, CoursesStack


class CoursesStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesStack
        fields = ('stack',)


class DurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duration
        fields = ('duration',)


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ('first_name', 'last_name', 'description', 'photo')


class CoursesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesImage
        fields = ('image',)


class TrialLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrialLesson
        fields = ('name', 'date', 'time', 'description')


class CourseSerializer(serializers.ModelSerializer):
    images = CoursesImageSerializer(many=True, read_only=True)
    courses_stacks = CoursesStackSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'why_we', 'description', 'images', 'courses_stacks')


class CourseDetailSerializer(serializers.ModelSerializer):
    durations = DurationSerializer(many=True, read_only=True)
    mentors = MentorSerializer(many=True, read_only=True)
    images = CoursesImageSerializer(many=True, read_only=True)
    courses_stacks = CoursesStackSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'why_we', 'description', 'durations', 'mentors', 'images', 'courses_stacks')


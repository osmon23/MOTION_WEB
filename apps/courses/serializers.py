from rest_framework import serializers
from .models import Course, Duration, Mentor, CoursesImage, TrialLesson


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
    class Meta:
        model = Course
        fields = ('id', 'name', 'why_we', 'description')


class CourseDetailSerializer(serializers.ModelSerializer):
    durations = DurationSerializer(many=True, read_only=True)
    mentors = MentorSerializer(many=True, read_only=True)
    images = CoursesImageSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'why_we', 'description', 'durations', 'mentors', 'images',)


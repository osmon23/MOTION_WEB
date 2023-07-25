from django.shortcuts import render

from .models import Course, TrialLesson
from .serializers import CourseSerializer, CourseDetailSerializer, TrialLessonSerializer

from rest_framework import generics


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer


class TrialLessonListView(generics.ListAPIView):
    queryset = TrialLesson.objects.all()
    serializer_class = TrialLessonSerializer

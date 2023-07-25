from django.urls import path

from .views import ContactListView, ApplicationCreateView


urlpatterns = [
    path('', ContactListView.as_view()),
    path('applications/', ApplicationCreateView.as_view()),
]

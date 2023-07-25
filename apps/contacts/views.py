from rest_framework import generics
from rest_framework import permissions

from .models import Contact, Application
from .serializers import ContactSerializer, ApplicationSerializer


class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all().order_by('name')
    serializer_class = ContactSerializer


class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all().order_by('first_name')
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.AllowAny]

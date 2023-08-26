from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255,
    )
    url = models.URLField(
        _('URL'),
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        _('Phone Number'),
        max_length=100,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')


class Application(models.Model):
    first_name = models.CharField(
        _('First Name'),
        max_length=100,
    )
    phone_number = models.CharField(
        _('Phone Number'),
        max_length=100,
    )
    email = models.EmailField(
        _('Email'),
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = _('Application')
        verbose_name_plural = _('Applications')


class Message(models.Model):
    chat_id = models.CharField(
        _('Chat ID'),
        max_length=100,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')

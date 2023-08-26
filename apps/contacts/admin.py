from django.contrib import admin

from .models import Contact, Application, Message


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'url',
        'phone_number',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'name',
        'url',
        'phone_number',
    )
    list_filter = (
        'name',
        'url',
        'phone_number',
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'phone_number',
        'email',
    )
    list_display_links = (
        'first_name',
    )
    search_fields = (
        'first_name',
        'phone_number',
        'email',
    )
    list_filter = (
        'first_name',
        'phone_number',
        'email',
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'chat_id',
    )
    list_display_links = (
        'chat_id',
    )
    search_fields = (
        'chat_id',
    )
    list_filter = (
        'chat_id',
    )
    readonly_fields = (
        'chat_id',
    )

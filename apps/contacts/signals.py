import datetime
import telebot

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)


@receiver(post_save, sender='contacts.Application')
def send_application_to_telegram(sender, instance, created, **kwargs):
    from .models import Message

    if created:
        message = f"Новая заявка!\n" \
                  f"Имя: {instance.first_name}\n" \
                  f"Телефон: {instance.phone_number}\n" \
                  f"Email: {instance.email}\n" \
                  f"Дата: {datetime.date.today()}"

        for profile in Message.objects.filter(subscribed=True):
            if profile is not None:
                bot.send_message(profile.chat_id, message)

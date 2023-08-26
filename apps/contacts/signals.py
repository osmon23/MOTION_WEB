import datetime
import telebot

from django.db.models.signals import post_save
from django.dispatch import receiver

from config import settings


bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)


@receiver(post_save, sender='contacts.Application')
def send_application_to_telegram(sender, instance, created, **kwargs):
    if created:
        message = f"Новая заявка!\n" \
                  f"Имя: {instance.first_name}\n" \
                  f"Телефон: {instance.phone_number}\n" \
                  f"Email: {instance.email}\n" \
                  f"Дата: {datetime.date.today()}"
        
        from .models import Message
        m_chat_id = Message.objects.all()
        for chat_id in m_chat_id:
            bot.send_message(chat_id.chat_id, message)

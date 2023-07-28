import datetime
import telebot

from django.db.models.signals import post_save
from django.dispatch import receiver

from config import settings


bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)

updates = bot.get_updates()


@receiver(post_save, sender='contacts.Application')
def send_application_to_telegram(sender, instance, created, **kwargs):
    if created:
        message = f"Новая заявка!\n" \
                  f"Имя: {instance.first_name}\n" \
                  f"Телефон: {instance.phone_number}\n" \
                  f"Email: {instance.email}\n" \
                  f"Дата: {datetime.date.today()}"

        chats_id = []

        for up in updates:
            chats_id.append(up.message.chat.id)
            print(up.message.chat.first_name)

        for chat_id in set(chats_id):
            bot.send_message(chat_id, message)
            print(chat_id)

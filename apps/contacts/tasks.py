from celery import shared_task

from .models import Message
from .signals import bot


@shared_task
def update_database():
    updates = bot.get_updates()
    for update in updates:
        if update is not None:
            Message.objects.get_or_create(
                name=update.message.chat.username,
                chat_id=update.message.chat.id,
            )

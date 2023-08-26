import telebot

from django.conf import settings
from django.core.cache import cache

from .models import Message


bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)

m_chat_id = Message.objects.all()

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    subscribe_button = telebot.types.KeyboardButton(text="Подписаться")
    unsubscribe_button = telebot.types.KeyboardButton(text="Отписаться")
    markup.add(subscribe_button, unsubscribe_button)
    bot.send_message(message.chat.id, "Добро пожаловать!", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Подписаться")
def subscribe(message):
    chat_id = message.chat.id
    cache.set(f'subscriber_{chat_id}', True)
    m_chat_id.create(chat_id=chat_id)
    print(m_chat_id.all())
    bot.send_message(chat_id, "Вы успешно подписались на рассылку!")

@bot.message_handler(func=lambda message: message.text == "Отписаться")
def unsubscribe(message):
    chat_id = message.chat.id
    cache.delete(f'subscriber_{chat_id}')
    if chat_id == m_chat_id.get(chat_id=chat_id):
        m_chat_id.delete(chat_id=chat_id)
    print(m_chat_id.all())
    bot.send_message(chat_id, "Вы успешно отписались от рассылки!")


bot.polling()

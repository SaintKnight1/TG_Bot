import telebot
from telebot import types

bot = telebot.TeleBot('6676623782:AAHaL32hiqxhpfDSu_IV_-8JKcx4-irndCo')

@bot.message_handler(content_types=['photo', 'audio'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Hello', callback_data='delete'))
    bot.reply_to(message, 'Обработка файла', reply_markup=markup)


@bot.message_handler()
def start(message):
    if message.text.lower() == 'лиза':
        bot.send_message(message.chat.id, 'Продам жопу за кокосово -банановое латте')
    else:
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')


# @bot.message_handler(commands=['start'])
# def main(message):  # message ранит в себе чат с пользователем
#     bot.send_message(message.chat.id, 'Привет!') # message.chat.id - это id текущего чата с пользователем

bot.infinity_polling() # позволяет не завершать работу скрипта, т.е. не останавливать бота

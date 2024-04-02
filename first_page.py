import telebot

bot = telebot.TeleBot('6676623782:AAHaL32hiqxhpfDSu_IV_-8JKcx4-irndCo')

@bot.message_handler(commands=['start'])
def main(message):  # message ранит в себе чат с пользователем
    bot.send_message(message.chat.id, 'Привет!') # message.chat.id - это id текущего чата с пользователем

bot.infinity_polling() # позволяет не завершать работу скрипта, т.е. не останавливать бота

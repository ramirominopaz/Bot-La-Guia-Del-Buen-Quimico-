from config import *
import telebot 

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=["start", "ayuda", "help"])
def command_start(message):
    bot.reply_to(message, "Que onda perri, todo piola?")

if __name__ == '__main__':
    print('Iniciamos el bot')
    bot.infinity_polling()
    print('Fin')

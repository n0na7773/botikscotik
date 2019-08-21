import config
import telebot
import time

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Здарова, ыыы")
#@bot.message_handler(commands=["help"])
#def start(message):
#    bot.send_message(message.chat.id, "/start - начало работы\n/help - помощь")
@bot.message_handler(commands=["seva"])
def start(message):
    bot.send_message(message.chat.id, "@seva_vilyatser, go nahuy")
@bot.message_handler(commands=["rip"])
def start(message):
    bot.send_message(message.chat.id, "Время смерти: " + time.ctime(time.time()))

if __name__ == "__main__":
    bot.polling(none_stop=True)

import telebot

bot = telebot.TeleBot('2073072113:AAG1sS32MedMhr3DpTyjCSd34iXuh-n39D8')

@bot.message_handler(content_types=['text'])
def start(message):
    bot.reply_to(message, "This is a message handler")

bot.polling()
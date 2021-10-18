from telebot import types

def makeUpTheMarkups(*props):
    markup = types.ReplyKeyboardMarkup()
    for item in props:
        markup.add(types.KeyboardButton(item))
    
    return markup

def removeTheMarkups(text, chat_id, bot):
    bot.send_message(chat_id, "Тренировка найдена", reply_markup=types.ReplyKeyboardRemove(selective=False))
import telebot
from telebot import types
from training_list import returnTheList as getTheTrainings

bot = telebot.TeleBot('2059612773:AAEBRiv3A0kzY80SISgEXxTVVwbjWrG8CsU')

def makeUpTheMarkups(*props):
    markup = types.ReplyKeyboardMarkup()
    for item in props:
        markup.add(types.KeyboardButton(item))
    
    return markup


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'test')
    chat_id = message.chat.id
    trainingsMenuCaller(chat_id)

def trainingsMenuCaller(chat_id):
    bot.send_message(chat_id, "Выберете тренировку", reply_markup=makeUpTheMarkups("Тренировка для новичков", "Тренировка для продвинутых"))
    
    @bot.message_handler(content_types=['text'])
    def mainMenuHandler(message):
        trainings = list(getTheTrainings().values())

        for i in trainings:
            if i["name"] == message.text:
                markup = types.ReplyKeyboardRemove(selective=False)
                bot.send_message(chat_id, "Тренировка найдена", reply_markup=markup)

        # for name, value in getTheTrainings()[message.text].items():
        #     print(name, value)
        # except:
        #     print("Except")

bot.polling()
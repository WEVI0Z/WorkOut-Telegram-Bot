import telebot
from training_list import returnTheList as getTheTrainings
from training_start import startTheTraining
from markups import *

bot = telebot.TeleBot('2059612773:AAEBRiv3A0kzY80SISgEXxTVVwbjWrG8CsU')

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
        targetTraining = []

        for i in trainings:
            if i["name"] == message.text:
                removeTheMarkups("Тренировка найдена", chat_id, bot)
                targetTraining = i
                
                startTheTraining(targetTraining, bot, chat_id)
        
        print("CHECKING___________________________________________________________________________")

bot.polling()
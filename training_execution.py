import telebot
from markups import *
import time

def startTheTraining(training, bot, chat_id, message):
    excersices = training["listOfExcersices"]

    def doAnExcersice(index):
        excercise = excersices[index]

        def enterTheRepeats(message):
            bot.send_message(message.chat.id, "Данные о повторениях записаны")

            if excercise["type"] == "repw":
                bot.send_message(message.chat.id, "Введите поднятый вес", reply_markup=makeUpTheMarkups("6 кг", "8 кг", "10 кг", "12 кг"))

                bot.register_next_step_handler(message, enterTheWeight)
            else:
                anotherStepStart(message)

        def enterTheWeight(message):
            bot.send_message(message.chat.id, "Данные о весе записаны")

            anotherStepStart(message)

        def enterTheTime(message):
            bot.send_message(message.chat.id, "Данные о времени выполнения записаны")

            anotherStepStart(message)
        
        def anotherStepStart(message):
            restTime = excercise["restTime"]

            bot.send_message(message.chat.id, "Перерыв, время для отдыха - " + str(restTime) + " секунд")

            time.sleep(restTime)

            bot.send_message(message.chat.id, "Хотите ли сделать еще один подход этого же упражения", reply_markup=makeUpTheMarkups("Да", "Нет"))
        
            bot.register_next_step_handler(message, anotherRepeatExecution)

        def anotherRepeatExecution(message):
            if message.text == "Да":
                doAnExcersice(index)
            elif index + 1 < len(excersices):
                doAnExcersice(index + 1)
            else:    
                bot.send_message(message.chat.id, "Тренировка завершена")

        def trainingChecking(message):
            if excercise["type"] == "rep" or excercise["type"] == "repw":
                bot.send_message(message.chat.id, "Введите кол-во повторений", reply_markup=makeUpTheMarkups("6 раз", "8 раз", "10 раз", "12 раз"))
                
                bot.register_next_step_handler(message, enterTheRepeats)
            else:
                bot.send_message(message.chat.id, "Введите время выполнения", reply_markup=makeUpTheMarkups("5 минут", "10 минут", "15 минут", "20 минут"))
                
                bot.register_next_step_handler(message, enterTheTime)

        bot.send_message(chat_id, "Приступите к выполнению упраженения " + excercise["name"].lower()
         + ". Когда закончите нажмите на кнопку 'Завершить'", reply_markup=makeUpTheMarkups("Завершить"))

        bot.register_next_step_handler(message, trainingChecking)    

    doAnExcersice(0)
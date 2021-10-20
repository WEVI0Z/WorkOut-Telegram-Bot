from markups import *
import time

def startTheTraining(training, bot, chat_id, message):
    excersices = training["listOfExcersices"]

    def enterTheRepeats(message):
        bot.send_message(message.chat.id, "Спасибо")

    def enterTheWeight(message):
        bot.send_message(message.chat.id, "Спасибо")

    def enterTheTime(message):
        bot.send_message(message.chat.id, "Спасибо")

    def doAnExcersice(index):
        excercise = excersices[index]

        def anotherRepeatExecution(message):
            if message.text == "Да":
                doAnExcersice(index)
            elif index + 1 < len(excersices):
                doAnExcersice(index + 1)
            else:    
                bot.send_message(message.chat.id, "Тренировка завершена")

        bot.send_message(chat_id, "Приступите к выполнению упраженения " + excercise["name"].lower()
         + ". Когда закончите нажмите на кнопку 'Завершить'", reply_markup=makeUpTheMarkups("Завершить"))
        
        if excercise["type"] == "rep" or excercise["type"] == "repw":
            bot.send_message(message.chat.id, "Введите кол-во повторений", reply_markup=makeUpTheMarkups("6 раз", "8 раз", "10 раз", "12 раз"))
            
            bot.register_next_step_handler(message, enterTheRepeats)
        else:
            bot.send_message(message.chat.id, "Введите время выполнения", reply_markup=makeUpTheMarkups("5 минут", "10 минут", "15 минут", "20 минут"))
            
            bot.register_next_step_handler(message, enterTheWeight)
        if excercise["type"] == "repw":
            bot.send_message(message.chat.id, "Введите поднятый вес", reply_markup=makeUpTheMarkups("5 кг", "10 кг", "15 кг", "20 кг"))
            
            bot.register_next_step_handler(message, enterTheTime)
        
        bot.send_message(message.chat.id, "Хотите ли сделать еще один подход этого же упражения", reply_markup=makeUpTheMarkups("Да", "Нет"))
        
        bot.register_next_step_handler(message, anotherRepeatExecution)
    
    doAnExcersice(0)
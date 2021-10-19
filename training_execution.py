from markups import *
import time

def startTheTraining(training, bot, chat_id, message):
    excersices = training["listOfExcersices"]
    
    def etirationOfExsercises(index):
        excersice = excersices[index]

        bot.send_message(chat_id, "Приступите к выполнению упраженения " + excersice["name"].lower() + ". Когда закончите нажмите на кнопку 'Завершить'", reply_markup=makeUpTheMarkups("Завершить"))
        
        
        def enterTheRepeats(message):
            bot.send_message(chat_id, "Введите кол-во повторений", reply_markup=makeUpTheMarkups("6", "8", "10", "12"))

            def enterTheWeight(message):
                bot.send_message(chat_id, "Введите поднятый вес", reply_markup=makeUpTheMarkups("5", "10", "15", "20"))

                def trainingEnding(message):
                    if index + 1 < len(excersices):
                        removeTheMarkups("Перерыв равен " + str(excersice["restTime"]) + " сек", chat_id, bot)
                        time.sleep(excersice["restTime"])

                        etirationOfExsercises(index + 1)
                    else:
                        bot.send_message(chat_id, "Тренировка завершена")

                bot.register_next_step_handler(message, trainingEnding)                

            bot.register_next_step_handler(message, enterTheWeight)

        bot.register_next_step_handler(message, enterTheRepeats)
    
    etirationOfExsercises(0)
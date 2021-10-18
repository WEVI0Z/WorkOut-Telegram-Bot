from markups import makeUpTheMarkups

# def enterTheNumber(message, text):


def startTheTraining(training, bot, chat_id):
    for exersice in training["listOfExcersices"]:
        print(exersice["name"])
        bot.send_message(chat_id, "Приступите к выполнению упраженения " + exersice["name"].lower() + ". Когда закончите нажмите на кнопку 'Завершить'", reply_markup=makeUpTheMarkups("Завершить"))

        a(bot, chat_id)

        print("PASSED")

        # @bot.message_handler(content_types=['text'])
        # def enterTheWeight(message):
        #     bot.send_message(chat_id, "Введите вес", reply_markup=makeUpTheMarkups("5", "10", "15", "20"))

def a(bot, chat_id):
    check = 0
    @bot.message_handler(content_types=['text'])
    def enterTheRepeats(message):
        bot.send_message(chat_id, "Введите кол-во повторений", reply_markup=makeUpTheMarkups("6", "8", "10", "12"))
        check = 1

    while(check != 1):
        print("something")
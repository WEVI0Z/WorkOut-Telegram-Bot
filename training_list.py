listOfTrainings = {
    "standartTraining" : {
        "name" : "Тренировка для новичков",
        "listOfExcersices" : [
            {
                "name" : "Отжимания",
                "instruction" : "Примите позу для отжиманий и отжимайтесь",
                "restTime" : 60,
                "AmountOfTimes" : 3
            },
            {
                "name" : "Приседания",
                "instruction" : "Выполняйте приседания",
                "restTime" : 60,
                "AmountOfTimes" : 3
            }
        ]
    },
    "intermediateTraining" : {
        "name" : "Тренировка для продвинутых",
        "listOfExcersices" : [
            {
                "name" : "Подтягивания",
                "instruction" : "Возьмите и подтягивайтесь",
                "restTime" : 60,
                "AmountOfTimes" : 3
            },
            {
                "name" : "Прыжки в длинну",
                "instruction" : "Выполняйте прыжки",
                "restTime" : 60,
                "AmountOfTimes" : 3
            }
        ]
    }
}

training = {
    "name" : "Тренировка по умолчанию"
}

#Переписать все снищу
def createTraining(name):
    training = {
        "name" : name,
        "listOfExcersices" : []
    }

    training.append(createTheExersice())

def createTheExersice(training, name, instruction, restTime = 60):
    exersice = {
        "name" : name,
        "instruction" : instruction,
        "restTime" : restTime
    }

    training["listOfExcersices"].append(exersice)


def returnTheList():
    return listOfTrainings
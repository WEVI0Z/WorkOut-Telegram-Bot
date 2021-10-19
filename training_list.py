listOfTrainings = {
    "standartTraining" : {
        "name" : "Тренировка для новичков",
        "listOfExcersices" : [
            {
                "name" : "Отжимания",
                "instruction" : "Примите позу для отжиманий и отжимайтесь",
                "restTime" : 5,
                "AmountOfTimes" : 3
            },
            {
                "name" : "Приседания",
                "instruction" : "Выполняйте приседания",
                "restTime" : 5,
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

def returnTheList():
    return listOfTrainings
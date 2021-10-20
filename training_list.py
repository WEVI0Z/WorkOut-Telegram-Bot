listOfTrainings = {
    "standartTraining" : {
        "name" : "Тренировка для новичков",
        "listOfExcersices" : [
            {
                "name" : "Отжимания",
                "instruction" : "Примите позу для отжиманий и отжимайтесь",
                "restTime" : 5,
                "type" : "rep"
            },
            {
                "name" : "Жим на горизонтальной скамье",
                "instruction" : "Лягьте на спину и выполняйте жим",
                "restTime" : 5,
                "type" : "repw"
            },
            {
                "name" : "Езда на тренажере",
                "instruction" : "Крутите педали",
                "restTime" : 5,
                "type" : "card"
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
                "type" : "rep"
            },
            {
                "name" : "Прыжки в длинну",
                "instruction" : "Выполняйте прыжки",
                "restTime" : 60,
                "type" : "rep"
            }
        ]
    }
}

def returnTheList():
    return listOfTrainings
import random
def playTheGame(userChoice, compChoice):
    choice = ["Камень", "Ножницы", "Бумага"]
    print("Ты выбрал: {0} Комп выбрал: {1}".format(choice[userChoice - 1], choice[compChoice - 1]))
    if userChoice - compChoice == 1 or userChoice - compChoice == -2:
        print("Комп выиграл")
    elif userChoice - compChoice == -1 or userChoice - compChoice == 2:
        print("Ты выиграл")
    else:
        print("Перекидывайте")

def getUserChoice():
    while True:
        print("Выбирай:")
        print("1. Камень")
        print("2. Ножницы")
        print("3. Бумага")
        try:
            userInput = int(input())
        except:
            print("Херню ввел")
            continue
        if userInput >=1 and userInput <=3:
            return userInput
        else:
            print("Херню ввел")
            continue

def getCompChoice():
    return random.randint(1, 3)

if __name__ == '__main__':
    while True:
        playTheGame(getUserChoice(), getCompChoice())


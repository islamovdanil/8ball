from random import randint
from time import sleep


response = [
    "Не сомневайся",
    "Определенно",
    "Будь уверен",
    "Да! Точно!",
    "Можно рассчитывать",
    "Думаю, да",
    "Скорее всего",
    "Есть перспективы",
    "Да",
    "Похоже, что да",
    "Возможно да",
    "Спроси позже",
    "Лучше промолчу",
    "Не могу сейчас определиться",
    "Конекретнее?",
    "Не надейся",
    "Я думаю - нет",
    "Не советую",
    "Не вижу хороших перспектив",
    "Очень сомнительно"
]


def ball():
    ques = str(input("Задай вопрос? \n").lower())
    print("Дай подумать...")
    sleep(1)
    idResponse = randint(0, 20)
    print(response[idResponse] + '\n\n')
    play()


def play():
    questionAgain = str(input("Еще вопрос? (y/n)\n").lower())
    if questionAgain == 'y':
        ball()

    elif questionAgain == 'n':
        print("До встречи!")

    else:
        print("Что это значит?")
        play()


if __name__ == '__main__':
    ball()
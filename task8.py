from random import randint
q = randint(0,100)
def num(i):
    a = int(input("Отгадайте число "))
    if a > q:
        print("Загаданное число меньше ")
    elif a < q:
        print("Загаданное число больше ")
    else:
        print("Вы отгадали ")
        return
    if i == 1:
        print("Вы не отгадали число ")
        print("Загаданное число: ", q)
    num(i-1)

num(10)
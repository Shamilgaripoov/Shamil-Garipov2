import math
def ingeener():

    op = int(input("Введите операцию: 1 - Power, 2 - root "))
    if op == 1:
        m = int(input("Введите число: "))
        n = int(input("Введите степень: "))
        print(math.pow(m, n))
    if op == 2:
        m = int(input("Введите число: "))
        print(math.sqrt(m))

ingeener()
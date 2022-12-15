import csv
num = int(input("Сколько записей ты хочешь добавить? "))
file = open("Books.csv", "a")
for x in range(0, num):
    Z = input("Новая запись: ")
    A = input("Автор записи: ")
    Y = input("Год издания: ")
    new_z = Z + ", " + A + ", " + Y + "\n"
    file.write(str(new_z))
file.close()
file = open ("Books.csv", "r")
search = input("Введи имя автора для поиска: ")
x = 0
for row in file:
    if search in str(row):
        print(row)
        count = x + 1
        if count == 0:
            print("Такого автора не существует!!!")

file.close()


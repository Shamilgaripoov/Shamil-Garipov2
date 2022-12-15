import csv
file = open("Books.csv", "a")
Z = input("Новая запись: ")
A = input("Автор записи: ")
Y = input("Год выпуска: ")
new_z = Z + "," + A + ", " + Y + "\n"
file.write(new_z)
file.close()
file = open("Books.csv", "r")
for row in file:
    print(row)
file.close()

import csv
file = list(csv.reader(open("Books.csv")))
Booklist = []
for row in file:
    Booklist.append(row)
x = 0
for row in Booklist:
    display = x, Booklist[x]
    print(display)
    x = x + 1
del_id = int(input("Введите номер строки которую хотите удалить: "))
del Booklist[del_id]
x = 0
for row in Booklist:
    display = x, Booklist[x]
    print(display)
    x = x + 1
A = int(input("Введите номер строки для изменения: "))
x = 0
for row in Booklist[A]:
    display = x, Booklist[A][x]
    print(display)
    x = x + 1
get_ch = int(input("Какую часть вы хотите изменить? "))
data = input("Введите новые данные: ")
Booklist[A][get_ch] = data
print(Booklist[A])
file = open("Books.csv", "w")
x = 0
for row in Booklist:
    new_zapis = Booklist[x][0] + ", " + Booklist[x][1] + ", " + Booklist[x][2] + "\n"
    file.write(newrecord)
    x = x + 1
file.close()

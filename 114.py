import csv
N = int(input("Начальный год: "))
E = int(input("Конечный год: "))
file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)
file = open("Books.csv", "w")
x = 0
for row in tmp:
    if int(tmp[x][2]) >= N and int(tmp[x][2]) <= E:
        print(tmp[x])
    x = x + 1

file.close()
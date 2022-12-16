import sqlite3
file = open("BooksList.txt", "w")

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT Name from Authors")
for x in cursor.fetchall():
    print(x)

selectauthor = input("Введите имя автора: ")

cursor.execute("SELECT * FROM Books WHERE Author = ?", [selectauthor])
for x in cursor.fetchall():
    record = str(x[0]) + " - " + x[1] + " - " + x[2] + " - " + str(x[3]) + "\n"
    file.write(record)

file.close()
db.close()
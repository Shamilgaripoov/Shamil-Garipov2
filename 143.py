import sqlite3
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

selectionyear = int(input("Введите год: "))

cursor.execute("""SELECT Books.Title, Books.DatePublished, 
Books.AuthorFROM Books WHERE DatePublished > ? ORDER BY DatePublished """, [selectionyear])

for x in cursor.fetchall():
    print(x)

db.close()
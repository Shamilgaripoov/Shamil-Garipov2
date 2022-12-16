import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT * FROM Authors")
for x in cursor.fetchall():
    print(x)

print()
place = input("Введите место рождения: ")

cursor.execute("""SELECT Books.Title, Books.DatePublished, Books.AuthorFROM Books,
Authors WHERE Authors.Name = Books.Author AND Authors.PlaceofBirth = ?)""", [place])

for x in cursor.fetchall():
    print(x)

db.close()
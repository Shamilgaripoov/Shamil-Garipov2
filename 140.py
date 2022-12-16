import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()


def new_phone():
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)


def get_phone():
    newid = int(input("Enter ID: "))
    newfname = int(input("Enter first name: "))
    newsname = int(input("Enter surname: "))
    newpnum = int(input("Enter phone number: "))
    cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber)
    VALUES (?, ?, ?, ?)""", (newid, newfname, newsname, newpnum))
    db.commit()


def add_surname():
    selectsurname = input("Enter a surname: ")
    cursor.execute(" SELECT * FROM Names WHERE surname = ?", [selectsurname])
    for x in cursor.fetchall():
        print(x)


def get_id_del():
    selectid = int(input("Enter ID: "))
    cursor.execute("DELETE FROM Names WHERE id = ?", [selectid])
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)
    db.commit()


with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()


def get_menu():
    again = "y"
    while again == "y":
        print()
        print("Main Menu")
        print()
        print("1) View phone book")
        print("2) Add to phone book")
        print("3) Search for surname")
        print("4) Delete person from phone book")
        print("5) Quit")
        print()
        selection = int(input("Enter your selection: "))
        print()

        if selection == 1:
            new_phone()
        elif selection == 2:
            get_phone()
        elif selection == 3:
            add_surname()
        elif selection == 4:
            get_id_del()
        elif selection == 5:
            again = "n"
        else:
            print("Incorrect selection entered")


get_menu()
db.close()
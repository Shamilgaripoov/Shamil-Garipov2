from tkinter import *

import csv

def create_new():

    file = open("people.csv", "w")
    file.close()

def save_list():

    file = open("people.csv", "a")
    name = name_box.get()
    age = age_box.get()
    new_people = name + ", " + age + "\n"
    file.write(str(new_people))
    file.close()
    name_box.delete(0, END)
    age_box.delete(0, END)
    name_box.focus()

window = Tk()
window.title("Люди")
window.geometry("450x150")

msg1 = Label(text = "Введите имя: ")
msg1.place(x = 20, y = 20, width = 100, height = 25)

name_box = Entry(text = "")
name_box.place(x = 120, y = 20, width = 100, height = 25)

name_box["justify"] = "left"
name_box.focus()

msg2 = Label(text = "Возраст: ")
msg2.place(x = 20, y = 50, width = 100, height = 25)

age_box = Entry(text = "")
age_box.place(x = 120, y = 50, width = 100, height = 25)
age_box["justify"] = "left"

button1 = Button(text = "Создать новый файл", command = create_new)
button1.place(x = 250, y = 20, width = 130, height = 25)

button2 = Button(text = "Добавить в файл", command = save_list)
button2.place(x = 250, y = 50, width = 130, height = 25)

window.mainloop()


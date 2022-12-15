from tkinter import *

import csv

def save_list():
    file = open("people.csv", "a")
    name = name_box.get()
    age = age_box.get()
    get_zapis = name + ", " + age + "\n"
    file.write(str(get_zapis))
    file.close()
    name_box.delete(0, END)
    age_box.delete(0, END)
    name_box.focus()

def read_list():
    name_list.delete(0, END)
    file = list(csv.reader(open("people.csv")))
    tmp = []
    for row in file:
        tmp.append(row)
        x = 0
    for i in tmp:
        data = tmp[x]
        name_list.insert(END, data)
        x = x + 1
window = Tk()
window.title("Люди")
window.geometry("450x150")

msg1 = Label(text = "Введите имя: ")
msg1.place(x = 20, y = 20, width = 100, height = 25)

name_box = Entry(text = "")
name_box.place(x = 120, y = 20, width = 100, height = 25)

name_box["justify"]="center"
name_box.focus()

msg2 = Label(text = "Возраст: ")
msg2.place(x = 20, y = 50, width = 100, height = 25)

age_box = Entry(text = "")
age_box.place(x = 120, y = 50, width = 100, height = 25)
age_box["justify"]="left"

button1 = Button(text = "Добавить",)
button1.place(x = 250, y = 20, width = 130, height = 25)

button2 = Button(text = "Прочитать", command = read_list)
button2.place(x = 250, y = 50, width = 130, height = 25)

msg3 = Label(text = "Сохранить: ")
msg3.place(x = 20, y = 80, width = 100, height = 25)

name_list = Listbox()
name_list.place(x = 120, y = 80, width = 230, height = 100)

window.mainloop()

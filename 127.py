from tkinter import *

def get_name():
    name = name_box.get()
    name_list.insert(END, name)
    name_box.delete(0, END)
    name_box.focus()

def clear_list():
    name_list.delete(0, END)
    name_box.focus()

window = Tk()
window.title("Имена: ")
window.geometry("450x150")

msg1 = Label(text = "Введи имя: ")
msg1.place(x = 20, y = 20, width = 100, height = 25)
name_box = Entry(text = 0)
name_box.place(x = 120, y = 20, width = 100, height = 25)
name_box.focus()

msg2 = Label(text = "Список имен: ")
msg2.place(x = 20, y = 80, width = 100, height = 25)
button1 = Button(text = "Добавить", command = add_name)
button1.place(x = 250, y = 20, width = 130, height = 25)
name_list = Listbox()

name_list.place(x = 120, y = 50, width = 100, height = 100)
button2 = Button(text = "Очистить", command = clear_list)
button2.place(x = 250, y = 50, width = 130, height = 25)

window.mainloop()


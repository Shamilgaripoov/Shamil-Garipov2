from tkinter import *
def get_list():
    name = namebox.get()
    namebox.delete(0, END)
    set_gender = gender.get()
    gender.set("Мужской/Женский")
    newdata = name + ", " + set_gender + "\n"
    name_list.insert(END, newdata)
    namebox.focus()
window = Tk()
window.title("Люди")
window.geometry("500x410")
msg1 = Label(text = "Введите имя: ")
msg1.place(x = 50, y = 50, width = 100, height = 25)

namebox = Entry(text = "")
namebox.place(x = 150, y = 50, width = 150, height = 25)
namebox.focus()

msg2 = Label(text = "Поле: ")
msg2.place(x = 50, y = 100, width = 100, height = 25)

gender = StringVar(window)
gender.set("Мужской/Женский")
gendermenu = OptionMenu(window, gender, "Мужской", "Женский")
gendermenu.place(x = 150, y = 100)

name_list = Listbox()
name_list.place(x = 150, y = 150, width = 150, height = 100)

but = Button(text = "Добавить в список", command = get_list)
but.place(x = 50, y = 300, width = 130, height = 25)

window.mainloop()

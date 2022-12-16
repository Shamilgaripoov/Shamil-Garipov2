from tkinter import*
def program():
 name = nym.get()
 set_gender = rt.get()
 a = name + ", " + set_gender + "\n"
 num.insert(END, a)
 nym.focus()
 file = open("people1.txt", "a")
 file.write(a)
 file.close()
 file = open("people1.txt", "r")
 print(file.read())
window = Tk()
window.title("Программа")
window.geometry("400x400")

msg1 = Label(text = "Введите имя: ")
msg1.place(x = 40, y = 45, width = 100, height = 35)

nym = Entry(text = "")
nym.place(x = 130, y = 45, width = 175, height = 35)
nym.focus()

msg2 = Label(text = "Выберите пол")
msg2.place(x = 50, y = 100, width = 100, height = 25)

rt = StringVar(window)
rt.set("Мужской/Женская")

geg = OptionMenu(window, rt, "Мужской", "Женская")
geg.place(x = 150, y = 100)

num = Listbox()
num.place(x = 140, y = 140, width = 160, height = 170)

qe = Button(text = "ПУСК!", command = program)
qe.place(x = 45, y = 350, width = 100, height = 25)

window.mainloop()

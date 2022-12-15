from tkinter import *

def programm():
    x = selection.get()
    y = x + ".gif"
    photo = PhotoImage(file = y)
    photobox.image = photo
    photobox["image"] = photo
    photobox.update()
window = Tk()
window.title("Программа")
window.geometry("400x450")

ph = PhotoImage(file = "ICU.gif")
photobox = Label(window, image = ph)
photobox.image = ph
photobox.place(x = 100, y = 20, width = 200, height = 150)

msg1 = Label(text = "Введите имя: ")
msg1.place(x = 50, y = 200, width = 100, height = 25)
selection = Entry(text = "")
selection.place(x = 200, y = 200, width = 100, height = 25)
selection.focus()

button = Button(text = "Программа", command = programm)
button.place(x = 150, y = 250, width = 100, height = 25)

window.mainloop()

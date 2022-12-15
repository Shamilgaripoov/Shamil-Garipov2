from tkinter import *

def click():
    name = textbox1.get()
    message = str("Hello " + name)
    textbox2["bg"] = "red"
    textbox2["fg"] = "Black"
    textbox2["text"] = message

window = Tk()
window.geometry("450x100")
label = Label(text = "Введите имя: ")
label.place(x = 30, y = 20)
textbox1 = Entry(text = "")

textbox1.place(x = 150, y = 20, width = 100, height = 25)

textbox1["justify"] = "center"
textbox1.focus()

button1 = Button(text = "Нажмите", command = click)
button1.place(x = 30, y = 50, width = 100, height = 25)
textbox2 = Message(text = "")
textbox2.place(x = 150, y = 50, width = 200, height = 30)

textbox2["bg"] = "white"
textbox2["fg"] = "black"

window.mainloop()

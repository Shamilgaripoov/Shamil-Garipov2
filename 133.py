from tkinter import *

def programma():
        name = textbox1.get()
        message = str("Hello " + name)
        textbox2["text"] = message
window = Tk()
window.title("Names")
window.geometry("450x350")
window.wm_iconbitmap("3qx4kqOLgtY.ico")
window.configure(background = "white")

logo = PhotoImage(file = "3qx4kQolGtY.gif")
msg1 = Label(image = logo)
msg1.place(x = 100, y = 20, width = 200, height = 150)
msg2 = Label(text = "Введите имя: ")
msg2.place(x = 30, y = 200)

msg2["bg"] = "red"
msg2["fg"] = "white"

textbox1 = Entry(text = "")
textbox1.place(x = 150, y = 200, width = 200, height = 25)

textbox1["justify"] = "center"
textbox1.focus()

button = Button(text = "Press me", command = programma)
button.place(x = 30, y = 250, width = 120, height = 25)

button["bg"] = "green"

textbox2 = Message(text = "")
textbox2.place(x = 150, y = 250, width = 200, height = 25)

window.mainloop()

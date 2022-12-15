from tkinter import *
import random

def click():

    Chislo = random.randint(1, 12)
    answer["text"] = Chislo
window = Tk()

window.title("Бросай кубик!")
window.geometry("150x200")

button1 = Button(text = "Бросить", command = click)
button1.place(x = 50, y = 50, width = 50, height = 25)

answer = Message(text = "")
answer.place(x = 60, y = 100, width = 30, height = 25)

window.mainloop()

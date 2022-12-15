from tkinter import *

import random

def progras():
    theirans = ansbox.get()
    theirans = int(theirans)
    x1 = msg2["text"]
    x1 = int(x1)
    x2 = msg2["text"]
    x2 = int(x2)
    sum = x1 + x2
    if theirans == sum:
        img = PhotoImage(file = "correct.gif")
        msg4.image = img
    else:
        img = PhotoImage(file = "wrong.gif")
        msg4.image = img
    msg4["image"] = img
    msg4.update()
def nextprogram():
    ansbox.delete(0, END)
    x1 = random.randing(10, 100)
    msg1["text"] = x1
    x2 = random.randing(10, 100)
    msg2["text"] = x2
    img = PhotoImage(file = "")
    msg4.image = img
    msg4["image"] = img
    msg4.update()
window = Tk()
window.title("Addition")
window.geometry("350x300")

msg1 = Label(text = "0")
msg1.place(x = 50, y = 30, width = 25, height = 25)

addsymbl = Message(text = "+")
addsymbl.place(x = 75, y = 30, width = 25, height = 25)
msg2 = Label(text = "0")
msg2.place(x = 100, y = 30, width = 25, height = 25)

msg3 = Message(text = "=")
msg3.place(x = 125, y = 30, width = 25, height = 25)

ansbox = Entry(text = "")
ansbox.place(x = 150, y = 30, width = 25, height = 25)
ansbox["justify"] = "center"
ansbox.focus()

checkbtn = Button(text = "Check", command = progras)
checkbtn.place(x = 50, y = 60, width = 75, height = 25)

nextbtn = Button(text = "Next", command = nextprogram)
nextbtn.place(x = 130, y = 60, width = 75, height = 25)

img = PhotoImage(file = "")
msg4 = Label(image = img)
msg4.image = img
msg4.place(x = 25, y = 100, width = 200, height = 150)
nextprogram()

window.mainloop()

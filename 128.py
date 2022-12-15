from tkinter import *

def get_rass():
    km = textbox1.get()
    km = int(km)
    mile = 0,6214
    kmvmile = km * mile
    textbox2.delete(0, END)
    textbox2.insert(END, kmvmile)
    textbox2.insert(END, "mile")

window = Tk()
window.title("Расстояние")
window.geometry("300x200")

msg = Label(text = "Введи число которое надо преобразовать: ")
msg.place(x = 30, y = 20)

textbox1 = Entry(text = "")
textbox1.place(x = 30, y = 50, width = 200, height = 25)

textbox1["justify"] = "center"
textbox1.focus()

convert1 = Button(text = "Преоброзовать милли в киллометр", command = get_rass)
convert1.place(x = 30, y = 80, width = 200, height = 25)

convert2 = Button(text = "Преобразовать киллометр в мили", command = get_rass)
convert2.place(x = 30, y = 110, width = 200, height = 25)

textbox2 = Entry(text = "")
textbox2.place(x = 30, y = 140, width = 200, height = 25)
textbox2["justify"] = "center"

window.mainloop()

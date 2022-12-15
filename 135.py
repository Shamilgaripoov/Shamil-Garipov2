from tkinter import *
def clicks():
    sel = set_color.get()
    window.configure(background = sel)
window = Tk()
window.title("Color")
window.geometry("200x200")

set_color = StringVar(window)
set_color.set("brown")
color_lst = OptionMenu(window, set_color, "Red", "purple", "Black", "Green", "Grey", "Yellow")

color_lst.place(x = 50, y = 30)
clickme = Button(text = "Нажмите", command = clicks)
clickme.place(x = 50, y = 150, width = 60, height = 30)

mainloop()

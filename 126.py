from tkinter import *

def get_on():
    num = enter_txt.get()
    num = int(num)
    answer = output_txt["text"]
    answer = int(answer)
    total = num + answer
    output_txt["text"] = total
def reset():
    total = 0
    output_txt["text"] = 0
    enter_txt.delete(0, END)
    enter_txt.focus()
total = 0
num = 0
window = Tk()
window.title("Сложение")
window.geometry("450x100")
enter_lbl = Label(text = "Введите число:")
enter_lbl.place(x = 50, y = 20, width = 100, height = 25)
enter_txt = Entry(text = 0)
enter_txt.place(x = 150, y = 20, width = 100, height = 25)

enter_txt["justify"] = "center"
enter_txt.focus()

add_btn = Button(text = "Добавить", command = get_on)
add_btn.place(x = 300, y = 20, width = 70, height = 25)

output_lbl = Label(text = "Ответ = ")
output_lbl.place(x = 50, y = 50, width = 100, height = 25)
output_txt = Message(text = 0)
output_txt.place(x = 150, y = 50, width = 100, height = 25)

output_txt["bg"] = "white"

clear_btn = Button(text = "Очистить", command = reset)
clear_btn.place(x = 300, y = 50, width = 70, height = 25)
window.mainloop()

file = open("Subject.txt", "w")
file = open("Subject.txt", "a")
file.write("1) Create a new file\n"
           "2) Display the file\n"
           "3) Add a new item to the file\n"
           "Make a selection 1, 2 or 3:\n")
file = open("Subject.txt", "r")
print(file.read())
while True:
    op = int(input("Что вы хотите сделать? \n"))
    if op == 1:
        school = input("Введи название школьного предмета: ")
        file = open("Subject.txt", "a")
        file.write(f"{school}\n")
        file = open("Subject.txt", "r")
        print(file.read())
        file.close()
    elif op == 2:
        file = open("Subject.txt", "r")
        print(file.read())
        file = open("Subject.txt", "r")
        print(file.read())
        file.close()
    elif op == 3:
        new_school = input("Введи новый школьный предмет: ")
        file = open("Subject.txt", "a")
        file.write(f"{new_school}\n")
        file = open("Subject.txt", "r")
        print(file.read())
        file.close()
def robot_hello():
    s = []
    while True:
        name = input("Введите ваше имя ")
        if name in s:
            print("Привет, " + name)
        else:
            print("Привет, " + name + " рад знакомству")
            s.append(name)


robot_hello()

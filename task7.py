def log():
    s = {}
    while True:
        login = input("Введите логин ")
        password = input("Введите пароль ")
        get_pass = s.get(login)
        if get_pass == password:
            print("Доступ разрешен")
        elif get_pass == None:
            print(f"Вы успешно зарегестрировались {login}")
            s[login] = password
        else:
            print("Доступ разрешен")


log()
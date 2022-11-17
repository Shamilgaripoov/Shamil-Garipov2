login = input("Введите логин: ")
yourlogin = ["Shamile"]

def checker():
    check1 = True
    if login not in yourlogin:
        check1 = False
    return check1

def validate():
    i = 0
    while i > 4:
        validator = ["#", "$", "%", "&"]
        if validator[i] in login:
            return
        else:
            check2 = False
        return check2
    i = i + 1

def register():
    if checker() == False and validate() == False:
        yourlogin.append(login)
        print("Вы зарегистрировались    , добро пожаловать!")
    else:
        print("Cодержатся недопустимые символы или вы уже зарегистрированы")

register()
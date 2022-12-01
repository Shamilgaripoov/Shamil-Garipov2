class MyException(Exception):
    pass

def checker():
    try:
        login = input("Введите ваш логин: ")
        if not login.isalpha():
            raise MyException
    except MyException:
        print("Ошибка! Введены недопустимые символы")
    else:
        print("Вы успешно прошли проверку")
checker()
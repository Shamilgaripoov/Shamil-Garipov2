logins = ["Shamile"]
passwords = ["1234"]

def login():
    urlogin = input("Введите логин: ")
    urpassword = input("Введите пароль: ")
    if urlogin not in logins or urpassword not in passwords or logins.index(urlogin) != passwords.index(urpassword):
        print("Доступ запрещён! ")
    elif logins.index(urlogin) == passwords.index(urpassword):
        print("Доступ разрешён! ")

def delete_user():
        deleterlogin = input("Введите логин, который хотите удалить: ")
        if deleterlogin in logins:
            logins.remove(deleterlogin)
        print("Логин ", deleterlogin , " был удалён".format(deleterlogin))

login()
delete_user()
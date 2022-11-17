def get_login():
    ulogin = input("Введите логин: ")
    return ulogin

def get_password():
    password = input("Введите пароль: ")
    polz = hash(password)
    return polz

print(get_login())
print(get_password())
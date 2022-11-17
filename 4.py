def get_password():
    password = input("Введите пароль: ")
    polz = hash(password)
    return polz

print(get_password())
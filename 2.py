import re

class MyException(Exception):
    pass

def check():
    x = input("Слово ")
    y = re.findall(r"[!@#$%^&*]")
    if y != []:
        raise MyException
    else:
        print("Ваш слоган ")

check()
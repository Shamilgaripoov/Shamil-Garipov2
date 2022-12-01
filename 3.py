import re


def find_email():
    names = re.findall(r'\w+@\w+.\w+', "Всем привет! Меня зовут Алексей. Мой email: alexVB@gmail.com. Привет, Алексей! Меня зовут Марина, моя почта: Marina@mail.ru")
    print(names)

find_email()

def validator():
    global y
    try:
        x = int(input("Введите число "))
        y = x * x
    except ValueError:
        print("Ошибка!!!!")
    else:
        print(y)
validator()
def reverse(a):
    if len(a) == 1:
        return a
    elif len(a) == 0:
        print("Вы ничего не ввели ")
    return a[-1] + reverse(a[:-1])


n = reverse(input("Введите слово: "))
print(n)

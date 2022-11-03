a = int(input("Введите число "))
def factorial(i,n):

    if i < a:
        i = i + 1
        n = n * i
        print(n)


        factorial(i,n)





factorial(0,1)
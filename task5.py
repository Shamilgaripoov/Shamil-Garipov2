def Fibonacci():
    f1 = f2 = 1
    while f1 < 100 and f2 < 100:
        f1, f2 = f2, f1 + f2
        print(f1)

Fibonacci()

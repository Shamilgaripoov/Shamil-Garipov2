def fib(N):
    f1, f2 = 0, 1
    for i in range(N, 0, -1):
        yield i
        f1, f2 = f2, f1 + f2
a = list(fib(10))
print(a)
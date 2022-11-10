def countdown(N):
    for i in range(N, 0, -1):
        yield i
gen = countdown(10)
while True:
    print(next(gen))
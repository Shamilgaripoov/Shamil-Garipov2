def abc(N):
    for i in range(N, 29, 1):
        yield i
gen = abc(1)
while True:
    print(next(gen))
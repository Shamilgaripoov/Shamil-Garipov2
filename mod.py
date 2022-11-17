def security():
    name = list(input(" "))
    for i in range(len(name)):
        name[i] = "*"
    print(name)
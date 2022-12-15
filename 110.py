file = open("Names.txt", "r")
file_list = [name.replace('\n',"") for name in file]
print(file_list)
file.close()
name = input("Введи имя из списочка: ")
if name in file_list:
    file1 = open("Names2.txt", "a")
    file1.write(f"{name} \n")
    file1 = open("Names2.txt", "r")
    print(file1.read())
    file1.close()
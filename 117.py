import csv
import random
x = 0
name = input("Ваше имя? ")
v1 = random.randint(10, 100)
v2 = random.randint(10, 100)
resh = str(v1) + " + " + str(v2) + " = "
otvet = int(input(resh))
otveti = v1 + v2
if otvet == otveti:
    record = x + 1
v1_1 = random.randint(10, 100)
v2_2 = random.randint(10, 100)
resh2 = str(v1_1) + " + " + str(v2_2) + " = "
otvet2 = int(input(resh2))
otveti2 = v1_1 + v2_2
if otvet == otveti2:
    a = x + 1
file = open("Game.csv", "a")
game_rec = name + "," + resh + "," + str(otvet) + "," + resh2 + ", " + str(otvet) + str(x) + "\n"
file.write(str(game_rec))
file.close()

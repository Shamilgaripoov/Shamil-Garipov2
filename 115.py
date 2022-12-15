import csv
file = open("Books.csv", "r")
a = 0
for row in file:
    display = "Row: " + str(a) + " - " + row
    print(display)
    b = a + 1
file.close()
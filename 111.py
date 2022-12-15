import csv
file = open("Books.csv", "w")
fld = "Книга, Автор, Год выпуска\n"
fl = "Книга\n"
book = "To Kill a Mockingbird, Harper Lee, 1960\n"
book1 = "A Brief History of Time, Stephen Hawking, 1988\n"
book2 = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
book3 = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
book4 = "Pride and Prejudice, Jan Austen, 1813\n"
file.write(str(fld))
file.write(str(book))
file.write(str(book1))
file.write(str(book2))
file.write(str(book3))
file.write(str(book4))
file = open("Books.csv", "r")
reader = csv.reader(file)
rows = list(reader)
print(rows [1])
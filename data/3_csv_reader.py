from csv import DictReader
with open("..//files/books-39204-271043.csv", newline='') as files_reader:
    reader = DictReader(files_reader)
    for row in reader:
        print(row['Title'])
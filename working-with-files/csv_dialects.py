import csv

with open('csv-files/passwd.csv', 'r') as f:
    reader = csv.reader(f, delimiter=':', lineterminator='\n')
    for row in reader:
        print(row)

print(csv.list_dialects())

csv.register_dialect('hashes', delimiter="#",
                     quoting=csv.QUOTE_NONE, lineterminator="\n")

with open('csv-files/items.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect="hashes")

    for row in reader:
        print(row)

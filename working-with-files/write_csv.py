import csv

with open("csv-files/people.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    csvdata = (5, "Alex", "Hungary")
    writer.writerow(csvdata)


with open("csv-files/numbers.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'x**2', 'x**3', 'x**4'])
    squares = [(x, x**2, x**3, x**4) for x in range(1, 101)]
    writer.writerows(squares)


with open("csv-files/numbers2.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'x**2', 'x**3', 'x**4'])
    for x in range(1, 101):
        row = (x, x**2, x**3, x**4)
        writer.writerow(row)

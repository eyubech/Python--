import csv
with open("FullYearTiming.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(" ".join(row))
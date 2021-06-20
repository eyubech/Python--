import csv

data = []

with open('FullYearTiming.csv"') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        data.append (row)

print("File has been read, and it has ", len(data), " lines.")
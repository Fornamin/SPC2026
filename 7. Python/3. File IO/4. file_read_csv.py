import csv

filename = '7. Python/File/data.csv'

# 1. legacy: list 
data = []
with open(filename, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)
print(data)

# 2. modern: dict
dict = []
with open(filename, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        dict.append(row)
print(dict)
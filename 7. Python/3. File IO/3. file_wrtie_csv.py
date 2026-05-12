import csv

data = [
    ['Name', 'Age', 'City'], # Heading: first line
    ['John', 23, 'Busan'],
    ['Jane', 25, 'Seoul'],
    ['Bob', 29, 'Busan']
]

filename = '7. Python/File/data.csv'

with open (filename, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

data2 = [
    {'Name': 'John', 'Age': 23, 'City': 'Busan'},
    {'Name': 'Jane', 'Age': 25, 'City': 'Seoul'},
    {'Name': 'Bob', 'Age': 29, 'City': 'Busan'}
]

with open(filename, 'w', newline='') as file:
    # header 추출
    headers = data2[0].keys()
    csv_writer = csv.DictWriter(file, fieldnames = headers)
    csv_writer.writeheader() # 첫 줄에 header 추가
    csv_writer.writerows(data2)
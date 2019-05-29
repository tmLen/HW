import csv

users = [{'name': 'Маша', 'age': 25, 'job': 'Scientist'}, {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},]

with open('export.csv', 'w', encoding='utf-8') as fout:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(fout, fields, delimiter=';')
    writer.writeheader()
    for user in users:
        writer.writerow(user)

import csv

with open("phonebook.csv", encoding = 'utf-8') as file:
    reader = csv.reader(file, delimiter = "|")
    phonebook = []
    for id in reader:
        phonebook.append(id)

# тестовые
print('весь список:', phonebook)
print('')
print('по индексу:', phonebook[1])
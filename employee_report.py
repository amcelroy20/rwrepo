import csv

infile = open('employee_data.csv', 'r')

csv_file=csv.reader(infile)

next(csv_file)
print('Highly Efficient Individuals:')

for line in csv_file:
    prod = int(line[5])
    hours = int(line[4])
    name = line[1]
    if prod/hours > 2:
        print(name)

print(f'\n')

infile.close()

infile = open('employee_data.csv', 'r')

csv_file=csv.reader(infile)

next(csv_file)

print('Low Efficiency Individuals:')

for line in csv_file:
    prod = int(line[5])
    hours = int(line[4])
    name = line[1]
    if prod/hours < 1:
        print(name)

print(f'\n')

infile.close()

infile = open('employee_data.csv', 'r')

csv_file=csv.reader(infile)

next(csv_file)

forties = []
thirties = []
twenties = []

for line in csv_file:
    age = int(line[2])
    name = line[1]
    if age >= 40:
        forties.append(name)
    elif 30 <= age <40:
        thirties.append(name)
    else:
        twenties.append(name)

print('Employees in their 40s:')

for i in forties:
    print(f'{i}')

print(f'\nTotal number of employees in their 40s: {len(forties)}')

print(f'\n')
print('Employees in their 30s:')

for i in thirties:
    print(f'{i}')

print(f'\nTotal number of employees in their 30s: {len(thirties)}')

print(f'\n')
print('Employees in their 20s:')

for i in twenties:
    print(f'{i}')

print(f'\nTotal number of employees in their 20s: {len(twenties)}')
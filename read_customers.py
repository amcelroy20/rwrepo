import csv

customers = open('customers.csv', 'r')

csv_file = csv.reader(customers)

#this will skip the first record
next(csv_file)

for rec in csv_file:
    #print(rec)
    print(f'First Name: {rec[1]} Last Name: {rec[2]}')
    input()
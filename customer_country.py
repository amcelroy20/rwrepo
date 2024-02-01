import csv

customers=open('customers.csv', 'r')

outfile=open('customer_country.csv', 'w')

csv_file = csv.reader(customers)

outfile.write('Full Name,Country\n')
next(csv_file)
num=0

for rec in csv_file:
    outfile.write(f'{rec[1]} {rec[2]},{rec[4]}\n')
    num+=1

outfile.write(f'# of records: {num}')
                  
customers.close()
outfile.close()
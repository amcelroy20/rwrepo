import csv

data=open('employee_data.csv','r')

csv_file=csv.reader(data)

next(csv_file)

for rec in csv_file:
    bonus = float(rec[3])*float(rec[7])
    pay = bonus + float(rec[3])
    print(f'Name: {rec[1]}\nSalary: $  {float(rec[3]):,.2f}\nBonus:  $   {bonus:,.2f}\nPay:    $  {pay:,.2f}')
    input()
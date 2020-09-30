#import budget data 
import os
import csv 
#working directory

csvpath=os.path.join('resourses','budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []
    
    print(f"Header: {csv_header}")               

#Months       
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    print(len(month))
 #Revenue 
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    print(total_revenue)

 #Avg Change
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
 # append profit_loss
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    #print(revenue_change)
    monthly_change = Total / len(revenue_change)
    print(monthly_change)
    #print(Total)
    
#Greatest Increase
    profit_increase = max(revenue_change)
    print(profit_increase)
    k = revenue_change.index(profit_increase)
    month_increase = month[k+1]
    
#Dependencies
import os
import csv

#variables / initial states
date = []
money = []

sum_total = 0

#reading csv
with open('PyBank/Resourses/budget_data.csv',newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
#for loop through data, appends lists, and increases counters
    for row in csvreader:
        date.append(row[0])
        money.append(int(row[1]))
        sum_total += float(row[1])
        #print(row)

#total months
months = len(date)

#loops through money indices and compares to find greates increase and decrease 
increase=money[0]
decrease=money[0]

for i in range(len(money)):
    if money[i] >= increase:
        increase = money[i]
        increase_month = date[i]
    elif money[i] <= decrease:
        decrease = money[i]
        decrease_month = date[i]
    else:
        print('Increase/Decrease Error')
        
#Average Profit/Loss Change
avg_money = round(sum_total/months, 2)

#Output file and print statments
with open('output_financial.txt',"w",newline = '') as textfile:
    print("Financial Analysis", file = textfile)
    print("-----------------------------------", file = textfile)
    print(f'Total Months: {months}', file = textfile)
    print(f'Total Revenue: ${sum_total}',file = textfile)
    print(f'Average Profit/Loss Change: ${avg_money}',file = textfile)
    print(f'Greatest Increase Profit/Loss: {increase_month}(${increase})',file = textfile)
    print(f'Greatest Decrease Profit/Loss: {decrease_month}(${decrease})',file = textfile)
    print("-----------------------------------", file = textfile)

with open('output_financial.txt', newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    for row in csvreader:
        print(row)

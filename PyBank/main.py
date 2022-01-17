from datetime import date
from decimal import Rounded
from functools import total_ordering
import os
import csv
from pydoc import describe
from sqlite3 import Row

#Create variables to store new data 
months = 0
revenue = []
total_revenue = 0
revenue_change = 0
monthly_change = []
total_profit_loss = 0
average_revenue_change = 0
Greatest_Increase_in_Profits = []
Greatest_Decresse_in_Profits = []
Increase_Date = []
Decrease_Date = []
Date = []
# To find path to read file
output_path = os.path.join("Resources", "budget_data.csv")
with open(output_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header= next (csvreader)
    

#Initialize loop
    for row in csvreader:
        Date.append(row[0])
        revenue.append(row[1])
        
        #To count total amount of "Ptofit/Losses"
        total_revenue = total_revenue + int(row[1])

#To count total months  
months = len(Date)        
print (months) 
print (total_revenue)        
                  
#To count the change in "Ptofit/Losses" 
i = 0
for i in range(len(revenue) - 1):
    revenue_change = int(revenue[i+1]) - int(revenue[i])
    monthly_change.append(revenue_change)
    total_profit_loss = sum(monthly_change)   
average_revenue_change = total_profit_loss / len(monthly_change)
average_revenue_change = (round(average_revenue_change,2))
print (average_revenue_change)

#To culculate Greatest_Increase_in_Profits
Greatest_Increase_in_Profits = max(monthly_change)
print (Greatest_Increase_in_Profits)

#To culculate Greatest_Decresse_in_Profits
Greatest_Decresse_in_Profits = min(monthly_change)
print (Greatest_Decresse_in_Profits)

#To culculate Increase profit date 
y = monthly_change.index(Greatest_Increase_in_Profits)
Increase_Date = Date[y+1]
print (Increase_Date)

#To culculate Decrease profit date
x = monthly_change.index(Greatest_Decresse_in_Profits)
Decrease_Date = Date[x+1]
print (Decrease_Date)


#To find path to WRITE file
analysis_path = os.path.join("analysis", "pybank_analysis.csv")

#Open file using "write" mode
with open(analysis_path, 'w') as datafile:

    #Initialize writer
    csvwriter = csv.writer(datafile)

    #Writing outcomes
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-------------------------------'])
    csvwriter.writerow(['Total Months: ' + str(months)])
    csvwriter.writerow(['Total: ' + '$' + str(total_revenue)])
    csvwriter.writerow(['Average Change: ' + '$' + str(average_revenue_change)])
    csvwriter.writerow(['Greatest Increase in Profits: ' + str(Increase_Date) + ' ($' + str(Greatest_Increase_in_Profits) + ')'])
    csvwriter.writerow(['Greatest Decrease in Profits: ' + str(Decrease_Date) + ' ($' + str(Greatest_Decresse_in_Profits) + ')'])







  

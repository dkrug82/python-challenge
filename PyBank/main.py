import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
os.chdir(dir_path)

budget_data = os.path.join("Resources", "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")
#print(budget_data)

print("Financial Analysis")
print("-----------------------")

totalMonthCount = 0
netTotal = 0
change = 0
lastMonth = 0
monthlyChange = []
months = []



with open(budget_data, "r", encoding="utf-8") as csvfile:
    csvReader = csv.reader(csvfile,delimiter=",")
    #print(csvReader)

    next(csvfile)
    for row in csvReader:
        if totalMonthCount == 0:
            firstMonth = row[1] #for average change
            
        totalMonthCount = totalMonthCount + 1 #for total months
        netTotal = netTotal + int(row[1]) #for total $ amount

        change = int(row[1])  - int(lastMonth) #for greatest increase/decrease

        monthlyChange.append(change) #for greatest increase/decrease
        
        lastMonth = row[1] #for greatest increase/decrease

        months.append(row[0]) #for greatest increase/decrease
   
    greatestIncrease = max(monthlyChange) #for greatest increase
    increaseIndex = (monthlyChange.index(greatestIncrease)) #for greatest increase

    greatestDecrease = min(monthlyChange)
    decreaseIndex = (monthlyChange.index(greatestDecrease))
    
    finalMonth = (row[1]) #for average change
    averageChange = (int(finalMonth) - int(firstMonth))/(totalMonthCount - 1)

#print(monthlyChange)
#print(change)
#print(secondMonth)
#print(greatestIncrease)
#print(monthIndex)
#print(greatestDecrease)
#print(decreaseIndex)
#print(months[44])

print("Total Months: " + str(totalMonthCount))
print("Total: $" + str(netTotal))
print("Average Change: $" + str(round(averageChange, 2)))
print(f'Greatest Increase in Profits: {months[increaseIndex]} (${greatestIncrease})')
print(f'Greatest Decrease in Profits: {months[decreaseIndex]} (${greatestDecrease})')


output_path = os.path.join("analysis", "financial_analysis.txt")

with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-----------------------\n")
    file.write(f'Total Months: {totalMonthCount}\n')
    file.write(f'Total: $ {netTotal}\n')
    file.write(f'Average Change: ${(round(averageChange, 2))}\n')
    file.write(f'Greatest Increase in Profits: {months[increaseIndex]} (${greatestIncrease})\n')
    file.write(f'Greatest Decrease in Profits: {months[decreaseIndex]} (${greatestDecrease})\n')

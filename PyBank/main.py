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


with open(budget_data, "r", encoding="utf-8") as csvfile:
    csvReader = csv.reader(csvfile,delimiter=",")
    #print(csvReader)

    next(csvfile)
    for row in csvReader:
        if totalMonthCount == 0:
            firstMonth = row[1]
            #secondMonth =  int(row[1]) #+ int(row[1])

        
        totalMonthCount = totalMonthCount + 1
        netTotal = netTotal + int(row[1])
        
        change = int(row[1])  - int(lastMonth)
        monthlyChange.append(change)
        lastMonth = row[1]

    #monthlyChange.append(change)   

    finalMonth = (row[1])
    averageChange = (int(finalMonth) - int(firstMonth))/(totalMonthCount - 1)

print(monthlyChange)
#print(change)
#print(monthlyChange)
#print(secondMonth)
#print("Total Months: " + str(totalMonthCount))
#print("Total: $" + str(netTotal))
#print("Average Cange: $" + str(round(averageChange, 2)))

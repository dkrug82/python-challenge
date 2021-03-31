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
counter = 0

with open(budget_data, "r", encoding="utf-8") as csvfile:
    csvReader = csv.reader(csvfile,delimiter=",")
    #print(csvReader)

    next(csvfile)
    #profitLoss = list(csvReader)
    #totalRows = len(profitLoss)

    #print(totalRows)

    for row in csvReader:
        if totalMonthCount == 0:
            firstValue = row[1]
        #print(row)
        totalMonthCount = totalMonthCount + 1
        netTotal = netTotal + int(row[1])
         
    secondValue = (row[1])
averageChange = int(firstValue - secondValue)/int(totalMonthCount - 1)

print("Total Months: " + str(totalMonthCount))
print("Total: $" + str(netTotal))
print(averageChange)
#print(lastValue)
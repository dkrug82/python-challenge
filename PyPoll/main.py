import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
os.chdir(dir_path)

election_data = os.path.join('Resources', 'election_data.csv')
print(election_data)

print("Election Results")
print("-----------------------")

totalVotes = 0
candidates = []

with open(election_data, "r", encoding="utf-8") as csvfile:
    csvReader = csv.reader(csvfile,delimiter=",")
    #print(csvReader)

    next(csvfile)

    for row in csvReader:
        totalVotes = totalVotes + 1

    #candidates = row[3]


#print(candidates)
print(f"Total Votes: {totalVotes}")
print("-----------------------")
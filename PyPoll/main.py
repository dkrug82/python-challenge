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
candidateVotes = []

with open(election_data, "r", encoding="utf-8") as csvfile:
    csvReader = csv.reader(csvfile,delimiter=",")
    #print(csvReader)
    #candidateVotes = (row[2])
    next(csvfile)
    
    
    
    for row in csvReader:
        totalVotes = totalVotes + 1 #for total votes
        candidateVotes.append(row[2])

    [candidates.append(x) for x in candidateVotes if x not in candidates]
        #if candidateVotes not in candidates:
            
            #candidates.append(candidateVotes)



    

#print(candidateVotes)
print(candidates)
print(f"Total Votes: {totalVotes}")
print("-----------------------")
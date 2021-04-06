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
#voteCount = []

with open(election_data, "r", encoding="utf-8") as csvfile:
    csvReader = csv.reader(csvfile,delimiter=",")
    #print(csvReader)
    #candidateVotes = (row[2])
    next(csvfile)
    
    
    
    for row in csvReader:
        totalVotes = totalVotes + 1 #for total votes
        
        #Candidate List
        candidateVotes.append(row[2])
    [candidates.append(x) for x in candidateVotes if x not in candidates]
       
        #if candidateVotes not in candidates:
    #candidateIndex = len(candidates)
    #votes = candidateVotes.count([0])
    #votes = candidateVotes.count(candidateIndex)
    #print(range(len(candidates)))
    #for votes in candidates:
    #votes = candidateVotes.count(candidates)
    
        #voteCount.append(votes)

            #candidates.append(candidateVotes)

    #Number of votes per candidate
    khanCount = candidateVotes.count(candidates[0])
    correyCount = candidateVotes.count(candidates[1])
    liCount = candidateVotes.count(candidates[2])
    otooleyCount = candidateVotes.count(candidates[3])

#Percentage Won
    khanPercent = round(int(khanCount) / int(totalVotes), 3) * 100
    correyPercent = round(int(correyCount) / int(totalVotes), 3) * 100
    liPercent = round(int(liCount) / int(totalVotes),3) * 100
    otooletPercent = round(int(otooleyCount) / int(totalVotes), 3) * 100

#print(khanPercent)
votePercent = [khanPercent, correyPercent, liPercent, otooletPercent]
voteCount = [khanCount, correyCount, liCount, otooleyCount]

winner = max(voteCount)
winnerIndex = voteCount.index(winner)
#print(winner)   
#candidateResults = {"cand"}
#electionResults = zip(candidates, votePercent, voteCount)


#print(votes)  
#print(khanCount)
#print(candidateVotes)
#print(voteCount)
#print(candidates)
print(f"Total Votes: {totalVotes}")
print("-----------------------")
#print(electionResults)
print(f'{candidates[0]}: {votePercent[0]}% ({voteCount[0]})')
print(f'{candidates[1]}: {votePercent[1]}% ({voteCount[1]})')
print(f'{candidates[2]}: {votePercent[2]}% ({voteCount[2]})')
print(f'{candidates[3]}: {votePercent[3]}% ({voteCount[3]})')
print("-----------------------")
print(f'Winner: {candidates[winnerIndex]}')

import os
import csv


#Initialize veriables to store data
votes = []
country = []
canditate = []
count = 0
name = []
vote_percentage = []
#To find reading path
output_path = os.path.join("Resources", "election_data.csv")
with open(output_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header= next (csvreader)

#Start loop
    for row in csvreader:
        count = count + 1
        canditate.append(row[2])

    for x in set(canditate):
        name.append(x)
        y = canditate.count(x)
        votes.append(y)
        n = (y/count) * 100
        n = (round(n,2))
        vote_percentage.append(n)

    winning_vote = max(votes)
    winner = name[votes.index(winning_vote)]

    print("Election Results")
    print("-----------------------")
    print("Total Votes: " + str(count))
    print("-----------------------")
    for i in range(len(name)):
        print(name[i] + ": " + str(vote_percentage[i]) + "% " + "(" + str(votes[i]) + ")")
    print("-----------------------")
    print("Winner: " + str(winner))
    print("-----------------------")

#To find path to WRITE file
election_path = os.path.join("analysis", "pypoll_analysis.txt")
with open (election_path, 'w') as text:
    text.write("Election Results\n")
    text.write("-----------------------\n")
    text.write("Total Votes: " + str(count) + "\n")
    text.write("-----------------------\n")
    for i in range(len(set(name))):
        text.write(name[i] + ": " + str(vote_percentage[i]) + "% " + "(" + str(votes[i]) + ")\n")
    text.write("-----------------------\n")
    text.write("Winner: " + str(winner) + "\n")
    text.write("-----------------------\n")
    


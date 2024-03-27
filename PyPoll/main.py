# Creating and reading files 
import os, csv
# Setting a path 
filepath = os.path.join("Resources", "election_data.csv")

with open(filepath, newline='') as csvfile:

    # reading the contents 
    csvR = csv.reader(csvfile, delimiter=',')

    # header
    csvX = next(csvR)

    clist = [candidate[2] for candidate in csvR]
    
# total votes
votes = len(clist)

# Creating and sorting the candidate list to determine the winner
candidatesData = [[candidate,clist.count(candidate)] for candidate in set(clist)]
candidatesData = sorted(candidatesData, key=lambda x: x[1], reverse=True)


# Printing the results

print("Election Results")
print("-------------------------")
print(f"Total Votes: {votes}")
print("-------------------------")

for candidate in candidatesData:
    votesPercentage = (candidate[1] / votes) * 100
    print(f'{candidate[0]}: {votesPercentage:6.3f}% ({candidate[1]})')

print("-------------------------")
print(f"Winner: {candidatesData[0][0]}")
print("-------------------------")

filepath = os.path.join("Analysis", "PyPoll_Results.txt")
with open(filepath, "w") as text_file:
    print("Election Results", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Total Votes: {votes}", file=text_file)
    print("-------------------------", file=text_file)

    for candidate in candidatesData:
        votesPercentage = (candidate[1] / votes) * 100
        print(f'{candidate[0]}: {votesPercentage:6.3f}% ({candidate[1]})', file=text_file)

    print("-------------------------", file=text_file)
    print(f"Winner: {candidatesData[0][0]}", file=text_file)
    print("-------------------------", file=text_file)
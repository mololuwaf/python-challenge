
#import modules
import csv
import os
import operator
pypoll_dataset = "./Resources/election_data.csv"

total_votes = 0 
#list of candidates
candidate_names = []
#candidate votes 
current_vote_share = []
#percentage of votes per candidate
vote_percent = []
counter = 0

with open(pypoll_dataset, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        #Total votes
        total_votes = total_votes +1 
        if row[2] not in candidate_names:
            candidate_names.append(row[2])
            index = candidate_names.index(row[2])
            current_vote_share.append(1)
        else:
            index = candidate_names.index(row[2])
            current_vote_share[index] += 1
    #Percent
    for votes in current_vote_share:
        percent = (votes/total_votes) * 100
        percent = round(percent)
        percent = "%.3f%%" % percent
        vote_percent.append(percent)

    #Winner
    winning_candidate = max(current_vote_share)
    index = current_vote_share.index(winning_candidate)
    President = candidate_names[index]

print(total_votes)
print(candidate_names)
print(current_vote_share)
print(vote_percent)


# printing Pypoll Results 
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidate_names)):
    print(f"{candidate_names[i]}: {str(vote_percent[i])} ({str(current_vote_share[i])})")
print("--------------------------")
print(f"Winner: {President}")
print("--------------------------")

# Exporttxtfile

output_text_file = "/Users/mollyfbg/PyPoll/Analysis/pyPollresult.txt"

pyPollresult = open(output_text_file, "w")

line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
pyPollresult.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidate_names)):
    line = str(
        f"{candidate_names[i]}: {str(vote_percent[i])} ({str(current_vote_share[i])})")
    pyPollresult.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {President}")
line7 = "--------------------------"
pyPollresult.write('{}\n{}\n{}\n'.format(line5, line6, line7))
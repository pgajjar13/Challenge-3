import csv
from collections import defaultdict

total_votes = 0
votes = defaultdict(int)

with open('PyPoll/Resources/election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader) # Skip header

    for row in csvreader:
        total_votes += 1
        votes[row[2]] += 1

output = (
    "Election Results\n"
    "-------------------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------------------\n"
)

election_winner = max(votes, key=votes.get)
for candidate_name, votes_count in votes.items():
    vote_percentage = (votes_count / total_votes) * 100
    output += f"{candidate_name}: {vote_percentage:.3f}% ({votes_count})\n"

output += (
    "-------------------------------------\n"
    f"Winner: {election_winner}\n"
    "-------------------------------------\n"
)



print(output)

with open('PyPoll/analysis/PyPoll_output.txt', 'w') as output_file:
    output_file.write(output)

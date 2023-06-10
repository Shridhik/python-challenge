import os
import csv

# Path to the input file
input_file = os.path.join("Resources", "election_data.csv")

# Path to the output file
output_file = os.path.join("analysis", "election_results.txt")

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(input_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Count the votes and track the candidates
    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        # If the candidate is already in the dictionary, increment their vote count
        if candidate in candidates:
            candidates[candidate] += 1
        # Otherwise, add the candidate to the dictionary with an initial vote count of 1
        else:
            candidates[candidate] = 1

# Determine the winner
for candidate, votes in candidates.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Calculate the percentage of votes each candidate won
candidate_percentages = {
    candidate: (votes / total_votes) * 100
    for candidate, votes in candidates.items()
}

# Generate the analysis output
output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

for candidate, votes in candidates.items():
    percentage = candidate_percentages[candidate]
    output += f"{candidate}: {percentage:.3f}% ({votes})\n"

output += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

# Print the analysis to the console
print(output)

# Write the analysis to the output file
with open(output_file, "w") as txtfile:
    txtfile.write(output)
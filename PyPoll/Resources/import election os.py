import os
import csv
path = r"C:\Users\pm300\Downloads\Starter_Code (6)\Starter_Code\PyPoll"
os.chdir(path)
election_csv = os.path.join("Resources", "election_data.csv")
# Read the CSV file
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip header row

    # Initialize variables
    total_votes = 0
    candidates = {}
    
    # Iterate through each row
    for row in csvreader:
        # Count total votes
        total_votes += 1

        # Extract candidate name from the row
        candidate = row[2]

        # Add candidate to the dictionary or increment their vote count
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculate the percentage of votes each candidate won
percentage_votes = {}
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    percentage_votes[candidate] = round(percentage, 2)

# Find the winner based on popular vote
winner = max(candidates, key=candidates.get)

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = percentage_votes[candidate]
    print(f"{candidate}: {percentage}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
# Write the results to a text file
filepath = os.path.join('Resources', 'PyPoll_Results.txt')
with open(filepath, 'w') as txtfile:
    print("Election Results",file = txtfile)
    print("-------------------------",file = txtfile)
    print(f"Total Votes: {total_votes}",file = txtfile)
    print("-------------------------",file = txtfile)
    for candidate, votes in candidates.items():
        percentage = percentage_votes[candidate]
        print(f"{candidate}: {percentage}% ({votes})",file = txtfile)
    print("-------------------------",file = txtfile)
    print(f"Winner: {winner}",file = txtfile)
    print("-------------------------",file = txtfile)

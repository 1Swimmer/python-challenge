import os
import csv

#Set path for file
csvvote = os.path.join("..","PyPoll","Resources","election_data.csv")

#print header of the output
print("Election Results")
print("-------------------------")

with open(csvvote, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #define header
    csv_header = next(csvreader)
    #print(csv_header)

    #Declaring variables
    votes = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []
    khan_votes =0
    correy_votes =0
    li_votes =0
    otooley_votes =0

  # Use for loop to read through rows and add the data to the newly defined lists
    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    #Total vote count
    total_votes = (len(votes))
    #print total_votes
    print (f"Total Votes:  {total_votes:.0f}")
    print(" -------------------------")

    #Votes count for each candidate
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)

   # Percentage votes of each candidate
    khan_percent = round((khan_votes / total_votes), 2)
    correy_percent = round((correy_votes / total_votes), 2)
    li_percent = round((li_votes / total_votes), 2)
    otooley_percent = round((otooley_votes / total_votes), 2)

#percentage and total number of votes each candidate won
    print(f"Khan: {khan_percent:.0%} {khan_votes:.0f}")
    print(f"Correy: {correy_percent:.0%} {correy_votes:.0f}")
    print(f"Li: {li_percent:.0%} {li_votes:.0f}")
    print(f"O'Tooley: {otooley_percent:.0%} {otooley_votes:.0f}")

#Winner 
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
    elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "OTooley"

    print(" -------------------------")
    print(f"Winner: {winner}")
    print(" -------------------------")

#create and output file
output_file = os.path.join("..","PyPoll","Analysis","Election_Results.txt")  

#  Open the output file 
file = open(output_file, "w") 

# Write information
file.write(f'Election results\n')
file.write(f'-------------------------\n')
file.write(f'Total Votes:  {total_votes:.0f}\n')
file.write(f'---------------------\n')
file.write(f'Khan: {khan_percent:.0%} {khan_votes:.0f}\n')
file.write(f'Correy: {correy_percent:.0%} ({correy_votes:.0f})\n')
file.write(f'Li: {li_percent:.0%} {li_votes:.0f}\n')
file.write(f'O´Tooley: {otooley_percent:.0%} ({otooley_votes:.0f})\n')
file.write(f'-------------------------\n')
file.write(f'Winner:{winner}\n')
file.write(f'-------------------------\n')
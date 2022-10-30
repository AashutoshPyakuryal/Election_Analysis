# Add Our dependencies.
from ast import For
import csv 
import os
from sqlite3 import Row
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Data Analysis Projects/Election_Analysis/Resources/election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("Data Analysis Projects/Election_Analysis/analysis/election_analysis.txt")

#1. Initialize a total vote counter.
total_votes = 0 

# Candidate Options
candidate_options = []

#1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data here. 
    # read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # print each row in the CSV file.
    for row in file_reader:
        #2 add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate... 
        if candidate_name not in candidate_options: 
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
            
         # Increment the votes by 1
        candidate_votes[candidate_name] += 1
            

# Determine the percentage of votes for each candidate by looping through the counts
#1. Iterate through the candidate list
for candidate_name in candidate_votes:
    #2. retrieve vote count of a candidate 
    votes = candidate_votes[candidate_name]
    #3. calculate the percentage of votes.
    vote_percentage = round((votes)/(total_votes) * 100, 1)
    #4. Print the candidate name and percentage of votes 
    print(f"{candidate_name}: received {vote_percentage}% of the vote.")
    
   
    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
                #2. If true then set winning_count = votes and winning_percent =
                #vote_percentage.
                winning_count = votes 
                winning_percentage = vote_percentage 
                #3. Set the winning_candidate equal to the candidate's name. 
                winning_candidate = candidate_name

# print out the winning candidate, vote count and percentage to
#   terminal.
print( f"{winning_candidate}: is the winning candidate with {winning_count} votes and {winning_percentage}% of the vote share.")


    
# Print the candidate vote dictionary







# Using the open 
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote 
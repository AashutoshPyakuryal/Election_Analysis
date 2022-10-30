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

    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal.
        election_results =  election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
       
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

#Print the candidate vote count to the terminal.
        for candidate_name in candidate_votes:
            # retrieve vote count and percentage
            votes = candidate_votes[candidate_name]
            vote_percentage = round((votes)/(total_votes) * 100, 1)
            candidate_results = (
                f"{candidate_name}: {vote_percentage}% ({votes:,})\n ")

            # Print each candidate's voter count and percentage to the terminal.
            print(candidate_results)
            # Save the candidate results to our text file
            txt_file.write(candidate_results)
            # Determine winning vote count, winning percentage, and winning candidate.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_candidate = candidate_name
                winning_percentage = vote_percentage
            # Print the winning candidate's results to the terminal 
            winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")
            print(winning_candidate_summary)
            # Save the winning candidate's results to the text file.
            txt_file.write(winning_candidate_summary)
            

            
        

    # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # print(winning_candidate_summary)

        
    # Print the candidate vote dictionary







    # Using the open 
    #1. The total number of votes cast
    #2. A complete list of candidates who received votes
    #3. The percentage of votes each candidate won
    #4. The total number of votes each candidate won
    #5. The winner of the election based on popular vote 
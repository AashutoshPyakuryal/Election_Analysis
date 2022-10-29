# Add Our dependencies.
import csv 
import os
# The data we need to retrieve.
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Data Analysis Projects/Election_Analysis/Resources/election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("Data Analysis Projects/Election_Analysis/analysis/election_analysis.txt")
# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data here. 
    # read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read and Print the header row.
    headers= next(file_reader)
    print(headers)





# Using the open 
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.
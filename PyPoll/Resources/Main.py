import os
import csv


#Loading the csv and my output file
csv_file = "Raw_data/election_data.csv"
output_file = "Analysis/election_analysis.txt"

#Creating my variables
vote_counter = 0
candidate_list = []
candidate_votes = {}
candidate_winner = ""
winning_votes = 0

# Reading the csv and converting it to a dictionary
with open(csv_file) as election_data:
    reader = csv.DictReader(election_data)
  
#Creating my for loop to extract name of candidate from each row
    for row in reader:
        vote_counter = vote_counter + 1
        candidate_name = row["Candidate"]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name]=candidate_votes [candidate_name] + 1
        else :
            candidate_votes[candidate_name]=candidate_votes [candidate_name] + 1
    
    print(candidate_votes)

#Printing my results to export to the text file
with open(output_file, "w") as txt_file:

#Creating my format for final vote count results
    moment_of_truth = (
        f"\n\nElection Results\n"
        f"---------------------\n"
        f"Total Votes: {vote_counter}\n"
        f"---------------------\n"
    )
    print(moment_of_truth)

#Saving the vote count to text file
    txt_file.write(moment_of_truth)

#I'm locating winner by looping through the candidate votes to get the vote count and percentage
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(vote_counter) * 100
#Now I'm tallying up the votes and identifying the winning candidate
        if(votes > winning_votes):
            winning_votes = votes
            candidate_winner = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
#Saving each candidates vote count and percentage to text file
        txt_file.write(voter_output)

#Announcing winning candidate
    the_winner_is = (
        f"--------------------\n"
        f"Winner: {candidate_winner}\n"
        f"--------------------\n"
    )
    print(the_winner_is)

#Saving winner output to text file
    txt_file.write(the_winner_is)


#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
#Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load=os.path.join("Resources", "election_results.csv")
#Create a filename variable to a direct or indirect path to the file.
file_to_save=os.path.join("Analysis", "election_analysis.txt")
#Using the with statement open the file as a text file
with open (file_to_save,"w") as txt_file:
    #Create a header for the file
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    #Write three counties to the file
    txt_file.write("Arapahoe\nDenver\nJefferson")

#Initialize the total vote counter.
total_votes=0
#Assign a variable for candidate name
candidate_options=[]
#Declare the empty dictionary
candidate_votes={}
#candidate_votes={"candidate_name1": votes, "candidate_name2": votes,"candidate_name3": votes}
#Winning candidate and winning count tracker
winning_candidate=""
winning_count=0
winning_percent=0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    #To do: read and analyze the data here
    #Read the file object with the reader function.
    file_reader=csv.reader(election_data)
    #Read the header row in the CSV file.
    headers=next(file_reader)
    #Print each row in the CSV file.
    for row in file_reader:
        #2 Add the total vote count.
        total_votes +=1
        #Print the candidate name for each row
        candidate_name=row[2]
        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)
            #Begin tracking votes for each candidate
            candidate_votes[candidate_name]=0
        #Add a vote to that candidate's total
        candidate_votes[candidate_name]+=1        
    
#Determine the percentage of votes for each candidate by looping through the count
#Iterate through the candidate list.
for candidate_name in candidate_votes:
    #Retrieve the vote count of the candidate
    votes=candidate_votes[candidate_name]
    #Calculate the percentage of votes.
    vote_percentage=(float(votes)/float(total_votes)*100)
    #Print the candidate name, vote count and percentage of votes.
    print(f"{candidate_name}: {votes:,} which is {vote_percentage:.1f}% of the vote.\n")
    #Determine winning vote count and candidate
    #1. Determine if the votes are greater than the winning count.
    if(votes>winning_count) and (vote_percentage>winning_percent):
        #2. If true then set winning_count = votes and winning_percent=vote_percentage
        winning_count=votes
        winning_percent=vote_percentage
        #3. Set the winning_candidate equal to the candidate's name.
        winning_candidate=candidate_name
    winning_candidate_summary=(
     f"----------------------\n"
     f"Winner: {winning_candidate}\n"
     f"Winning Vote Count:{winning_count:,}\n"
     f"Winning Percentage:{winning_percent:.1f}%\n"
     f"-----------------------\n")
print (winning_candidate_summary)      
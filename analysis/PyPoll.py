# the data we need to retrieve
#1. the total number of votes cast
#2. A complete list of candidates who recieved votes
#3. the percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
#import the datetime class from the datetime module

#assign a variable for the file to load and the path.
import csv
import os

#Assign variable to load a file from a path
file_to_load=os.path.join("Election_Analysis_","Resources original","election_results.csv")
#Assign variable to save a file from a path
file_to_save=os.path.join('Election_Analysis_','analysis','election_analysis.txt')
#1. intialize a total vote counter.
total_votes=0

#candidate Options
candidate_options=[]
#1. Declare an empty dictionary.
candidate_votes={}

#Winning Candidate and Winning Count Tracker
winning_candidate=""
winning_count=0
winning_percentage=0

#Open the election results and read the file.
with open(file_to_load) as election_data:
   file_reader=csv.reader(election_data)

   #read the header row
   headers=next(file_reader)

   #print each row in CSV file
   for row in file_reader:

      #2.add to the total vote count
      total_votes+=1

      #Print the Candidate Options
      candidate_name=row[2]

   #If candidate does not match any existing candidate...
      if candidate_name not in candidate_options:

         #Add the candidate name to the candidate list.
         candidate_options.append(candidate_name)

   #2. begin tracking that candidates vote count
         candidate_votes[candidate_name]=0

   #Add a vote to that candidates count.
      candidate_votes[candidate_name]+=1

   #Add a vote to that candidate's count
with open(file_to_save,"w") as txt_file:
      election_results=(
         f"\nElection Results\n"
         f"---------------------\n"
         f"Total votes: {total_votes:,}\n"
         f"---------------------\n")
      print(election_results,end="")
      #Save the final vote count
      txt_file.write(election_results)

   #1. Iterate through the candidate list

      for candidate_name in candidate_votes:
         #2.Retrieve vote count of a candidate_name
         votes=candidate_votes[candidate_name]
         #3. calculate the percentage of votes.
         vote_percentage=float(votes)/float(total_votes)*100
         candidate_results=(
            f"{candidate_name}: {vote_percentage:.1f}%({votes:,})\n")
   # to do: print out the winning candidate, vote count and percentage to
      #terminal.
         print(candidate_results)
         txt_file.write(candidate_results)
         if(votes>winning_count)and(vote_percentage>winning_percentage):
            #if true then set winning_count=votes and winning_percent=
            winning_count=votes
            winning_percentage=vote_percentage
            #and set the winning_candidate equal to the candidates name.
            winning_candidate=candidate_name

            
      winning_candidate_summary=(
         f"----------------------\n"
         f"Winner:{winning_candidate}\n"
         f"Winning Vote Count: {winning_count:,}\n"
         f"Winning Percentage: {winning_percentage:.1f}%\n"
         f"----------------------\n")
      print(winning_candidate_summary)
      #save the winning candidates results to the text file.
      txt_file.write(winning_candidate_summary)
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


#Open the election results and read the file.
with open(file_to_load) as election_data:
# to do: read and analyze data here.
   file_reader=csv.reader(election_data)
#print each row in the CSV file.
   headers=next(file_reader)
   print(headers)
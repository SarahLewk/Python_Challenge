import os
import csv

csvpath = os.path.join('..',"Resources","election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile)   
    

#I'm trying to figure out how to open this large csvfile with all of the data included

#1) Count how many votes in total (Does each voter ID# count as a vote?)
#   I couldn't get the file to open fully so I can't see all of the data so
#   I psuedo coded what I could
def getVotes(voterData):
totalVotes = int(voterData[1]) + #guessing since I can't see the columns

#2) Count how many candidates recieved votes

#3) % each candidate won

#4) Total number of votes each candidate won

#5) Calculate winner by popular vote


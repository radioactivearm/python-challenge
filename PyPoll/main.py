## Andy McRae
## PyPoll

# This script helps modernize the vote counting process

#---------------------------------------
# import modules
import os
import csv


#-----------------------------------------------------
# functions

# count number of votes
def count_poll(vote):
    # i assuming no repeated votes
    count = len(vote)
    return count

    



#--------------------------------------------------
# open and read csv file into a dictionary of lists

# create path to csv file
csvpath = os.path.join('Resources','election_data.csv')

# open csv for reading
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    # print(csvreader)

    # Take header from file and make keys
    keys_comma = next(csvfile)
    keys = keys_comma.split(',')
    keys[2] = keys[2].replace('\n','')
    # print(keys)
    
    # creating dictionary with headers as keys
    # keys[0] = 'Voter ID', keys[1] = 'County', keys[2] = 'Candidate'
    poll = {}
    poll[keys[0]] = []
    poll[keys[1]] = []
    poll[keys[2]] = []

    # read rest of file into dictionary
    for row in csvreader:
        poll[keys[0]].append(row[0])
        poll[keys[1]].append(row[1])
        poll[keys[2]].append(row[2])

    print(len(poll[keys[1]]))



print(f'Total Votes: {count_poll(poll[keys[0]])}')







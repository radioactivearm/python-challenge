## Andy McRae
## PyPoll

# This script helps modernize the vote counting process

#---------------------------------------
# import modules
import os
import csv
import numpy as np


#-----------------------------------------------------
# functions

# count number of votes
def count_poll(vote):
    # i assuming no repeated votes
    count = len(vote)
    return count


# find candidates
# building on this one, making it find number of votes as it finds candidates
def candidates(candidates):
    
    runner = []
    
    # i am thinking that there is something about how list comprehension works that is alluding me here
    # because this just does not work
    # found_candi = [candidates.pop() for candi in candidates if candi not in found_candi]

    # finds all unique candidates
    for candi in candidates:
        # if they are not already in list of unique candidates, this will add them
        if candi not in runner:
            runner.append(candi)


    # returns list of candidates
    return runner

# this function is going to calculate total
def totaling_vote(votes,num_of_candi):

    # creating a list of zeros equal to length of candidates; imported numpy for this :)
    total_votes = np.zeros(len(num_of_candi))

    #loop thru all votes casted
    for vote in votes:
        # loop thru all candidates
        for candi in num_of_candi:
            # and check which candidate the vote was cast for
            if vote == candi:
                # then tally that vote under the candidates slot
                total_votes[num_of_candi.index(candi)] += 1

    # returns a list that corresponds with candidate list
    return total_votes

    



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

print(candidates(poll[keys[2]]))

list_of_candidates = candidates(poll[keys[2]])

print(totaling_vote(poll[keys[2]],list_of_candidates))








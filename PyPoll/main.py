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


# calulates percent of votes each candidate got.
def percent_vote(all_votes,total_votes):
    percent_wins = (total_votes / all_votes) * 100

    return percent_wins


# finds and returns wich candidate had the greatest total number of votes cast in their name
def winner(candidate,total_votes):

    # stores the candidates name who as most votes
    winner_winner = ''
    # stores most votes tied to candidate
    winner_total = 0

    # runs thru all candidates
    for i in range(len(candidate)):
        # compares all vote counts
        if total_votes[i] > winner_total:
            winner_winner = candidate[i]
            winner_total = total_votes[i]

    # returns candidate name (string)
    return winner_winner

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

    # print(len(poll[keys[1]]))


# making variable for total votes cast
# print(f'Total Votes: {count_poll(poll[keys[0]])}')
total_votes = count_poll(poll[keys[0]])

# making list of all candidates
# print(candidates(poll[keys[2]]))
list_of_candidates = candidates(poll[keys[2]])

# making list of total votes for each candidates
# print(totaling_vote(poll[keys[2]],list_of_candidates))
list_of_totals = totaling_vote(poll[keys[2]],list_of_candidates) 

# making list of percentage of total votes each candidate got
# print(percent_vote(total_votes,list_of_totals))
list_of_percents = percent_vote(total_votes,list_of_totals)

# which candadate won
# print(winner(list_of_candidates,list_of_totals))
winner_of_poll = winner(list_of_candidates,list_of_totals)


#----------------------------------------------------------------------------------
# Printing results

print('Election Results')
print('------------------------------')

# printing total votes
print(f'Total Votes: {count_poll(poll[keys[0]])}')
print('------------------------------')

# printing main block of text once for each candidate (added two zeros because git is not printing all the zeros)
for i in range(len(list_of_candidates)):
    print(f'{list_of_candidates[i]}: {list_of_percents[i]:.3f}% ({list_of_totals[i]:.0f})')

print('------------------------------')

# prints winner of whole thing
print(f'Winner: {winner_of_poll}')
print('------------------------------')







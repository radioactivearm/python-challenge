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

# find candidates
# building on this one, making it find number of votes as it finds candidates
def candidates(candidates):
    
    runner = {}

    # finds all unique candidates
    for candi in candidates:
        # if they are not already in list of unique candidates, this will add them
        if candi not in runner:
            runner[candi] = candi

    # returns list of candidates
    return runner

# this function is going to calculate total returns a dictionary
def totaling_vote(votes):

    dict_of_candi = {}

    for vote in votes:
        if vote not in dict_of_candi:
            dict_of_candi[vote] = 1
        else:
            dict_of_candi[vote] += 1

    return dict_of_candi

# calulates percent of votes each candidate got returns dictionary
def percent_vote(all_votes,total_votes):

    percent_wins = {}
    for vote in total_votes:
        percent_wins[vote] = (int(total_votes[vote]) / int(all_votes)) * 100 

    return percent_wins

# finds and returns wich candidate had the greatest total number of votes cast in their name
def winner(candidate,total_votes):

    # stores the candidates name who as most votes
    winner_winner = ''
    # stores most votes tied to candidate
    winner_total = 0

    # runs thru dict of all candidates
    for vote in candidate:
        if total_votes[vote] > winner_total:
            winner_winner = vote
            winner_total = total_votes[vote]

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

#---------------------------------------------------------
# using functions

# making variable for total votes cast
total_votes = count_poll(poll[keys[0]])

# making list of all candidates
dict_of_candidates = candidates(poll[keys[2]])

# making list of total votes for each candidates
dict_of_totals = totaling_vote(poll[keys[2]]) 

# making list of percentage of total votes each candidate got
dict_of_percents = percent_vote(total_votes,dict_of_totals)

# which candadate won
winner_of_poll = winner(dict_of_candidates,dict_of_totals)

#---------------------------------------------------------------------------------
# making a formatted string of for printing and writing

#breaking in two so i can run a list comprehension in the middle
poll_summary_1 = (
    f'Election Results\n'
    f'------------------------------\n'
    f'Total Votes: {count_poll(poll[keys[0]])}\n'
    f'------------------------------'
)

poll_summary_2 = (
    f'------------------------------\n'
    f'Winner: {winner_of_poll}\n'
    f'------------------------------'
)

#---------------------------------------------------------------
# print

print(poll_summary_1)
[print(f'{dict_of_candidates[candi]}: {dict_of_percents[candi]:.3f}% ({dict_of_totals[candi]:.0f})') for candi in dict_of_candidates]
print(poll_summary_2)

#----------------------------------------------------------------
# write to txt file poll_summary
polling = open('analysis/poll_summary.txt', 'w')
polling.write(poll_summary_1)
polling.write('\n')
[polling.write(f'{dict_of_candidates[candi]}: {dict_of_percents[candi]:.3f}% ({dict_of_totals[candi]:.0f})\n') for candi in dict_of_candidates]
polling.write(poll_summary_2)
polling.close()

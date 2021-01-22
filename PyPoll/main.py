## Andy McRae
## PyPoll

# This script helps modernize the vote counting process

#---------------------------------------
# import modules
import os
import csv

#-----------------------------------------------------
# functions

# find candidates
# building on this one, making it find number of votes as it finds candidates
def candidates(candidates):
    
    runner = {}

    # finds all unique candidates
    for candi in candidates:
        # if they are not already a key, this will add them(as a key to themselves)
        if candi not in runner:
            runner[candi] = candi

    # returns dictionary of candidates
    return runner

# this function is going to calculate total returns a dictionary
def totaling_vote(votes):

    #create an empty dictionary to be filled with keys of candidates and values
    #  of how many votes they got
    dict_of_candi = {}

    # runs thru all votes
    for vote in votes:
        #if candidate not a key, they are added and vote count is set at 1
        if vote not in dict_of_candi:
            dict_of_candi[vote] = 1
        # if they are a key, their count is incremeted by 1
        else:
            dict_of_candi[vote] += 1
    
    # returns a dictionary
    return dict_of_candi

# calulates percent of votes each candidate got returns a dictionary
def percent_vote(all_votes,total_votes):

    percent_wins = {}

    # go over all candidates total vote count and calculate percent vote
    for vote in total_votes:
        percent_wins[vote] = (int(total_votes[vote]) / int(all_votes)) * 100 

    # returns dictionary
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

#---------------------------------------------------------
# using calculation figures, using functions and assigning them to variables

# calculating total votes
total_votes = len(poll[keys[0]])

# making dictionary of all candidates
dict_of_candidates = candidates(poll[keys[2]])

# making dictionary of total votes for each candidates
dict_of_totals = totaling_vote(poll[keys[2]]) 

# making dictionary of percentage of total votes each candidate got
dict_of_percents = percent_vote(total_votes,dict_of_totals)

# which candadate won
winner_of_poll = winner(dict_of_candidates,dict_of_totals)

#---------------------------------------------------------------------------------
# making a formatted string of for printing and writing

#breaking in two so i can run a list comprehension in the middle
poll_summary_1 = (
    f'Election Results\n'
    f'------------------------------\n'
    f'Total Votes: {total_votes}\n'
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
txtpath = os.path.join('analysis','poll_summary.txt')
polling = open(txtpath, 'w')
polling.write(poll_summary_1)
polling.write('\n')
[polling.write(f'{dict_of_candidates[candi]}: {dict_of_percents[candi]:.3f}% ({dict_of_totals[candi]:.0f})\n') for candi in dict_of_candidates]
polling.write(poll_summary_2)
polling.close()

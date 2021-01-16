## Andy McRae
## PyBank

# This script analyzes finacial records for my company

#--------------------------------------------------------
# import modules
import os
import csv

#-----------------------------------------------------------
# functions

# find total number of months
def total_months(date,profit):

    # pass in lists
    totals = len(date)
    
    # returns to total
    return totals

# Sums the profit/losses
def sum_profit(profit):

    # pass in list
    total = 0

    # goes thru list and sums the contents
    # (turns them into integers since I can't assume
    #  that they already are)
    for i in profit:
        total += int(i)

    # returns the sum 
    return(total)

# finds average change in profits/losses over the years
def changes(profit):

    # need the length to iterate over but minus one since i am looking
    # ahead one already in my loop
    length = len(profit) - 1

    # where i will tally up total changes over the course of the time
    total = 0
    for i in range(length):
        this_month = int(profit[i])
        next_month = int(profit[i+1])
        change = next_month - this_month
        total += change
    
    # I am dividing by the length - 1 since there is one less object in this new set
    average_change = round((total / (len(profit) - 1)), 2)

    # returns the average change
    return average_change
            

#-----------------------------------------------------------
# open and read file into a dictionary of lists

# creating path to csv file
csvpath = os.path.join('Resources','budget_data.csv')

# opening csv file for reading
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # taking the header from csv file and using them
    # to create keys in a dictionary
    keys_comma = next(csvfile)
    keys = keys_comma.split(',')
    keys[1] = keys[1].replace('\n','')
    # print(keys)
    
    # creating dictionary with headers as keys
    # keys[0] = 'Date' , keys[1] = 'Profit/Losses'
    finance = {}
    finance[keys[0]] = []
    finance[keys[1]] = []
    # print(finance)

    # read rest of file into lists which will be put into dictonary
    for row in csvreader:
        finance['Date'].append(row[0])
        finance['Profit/Losses'].append(row[1])

    # print(finance['Date'][-1])
    # print(len(finance['Date']))


#----------------------------------------------------------------------
# use functions on dictionary to find desired values (and save them)

# # use total_months on dictionary
tot_mon = total_months(finance['Date'],finance['Profit/Losses'])

# # use sum_profit on dictionary
sum_prof = sum_profit(finance['Profit/Losses'])

# use changes on dictionary
avg_change = changes(finance['Profit/Losses'])


#----------------------------------------------------------------------------
# Print Out A nice summary of findings
print('Financial Analysis')
print('----------------------------')
#printing a formating string of total months
print(f'Total Months: {tot_mon}')
# printing a formated string of total profits
print(f'Total: ${sum_prof}')
# printing a formatted string of average change
print(f'Average Change: ${avg_change}')
    
## Andy McRae
## PyBank

# This script analyzes finacial records for my company

# import modules
import os
import csv


#-----------------------------------------------------------
# functions

# find total number of months
def total_months(date,profit):
    # pass in lists
    totals = len(date)
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
    return(total)



#-----------------------------------------------------------


# creating path to csv file
csvpath = os.path.join('Resources','budget_data.csv')

# opening csv file for reading
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # taking the header from csv file and using them
    # to create keys in a dictionary
    keys_comma = next(csvfile)
    keys = keys_comma.split(',')
    keys[1] = keys[1].replace('\n','')
    print(keys)
    
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

    print(finance['Date'][-1])
    print(len(finance['Date']))

# use total_months on dictionary
print(total_months(finance['Date'],finance['Profit/Losses']))

# use sum_profit on dictionary
print(sum_profit(finance['Profit/Losses']))
    
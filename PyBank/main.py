## Andy McRae
## PyBank

# This script analyzes finacial records for my company

#--------------------------------------------------------
# import modules
import os
import csv

#-----------------------------------------------------------
# functions

# Sums the profit/losses
def sum_profit(profit):

    # pass in list
    total = 0

    # goes thru list and sums the contents
    # (turns them into integers since I can't assume
    # that they already are)
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
            
# finds the greatest increase in profits (date and amount)
# over the entire period
# return in form of dictionary with keys of month and change
def great_inc(date,profit):

    # These are my intial place holders for greatest values
    great_date = ''
    great_change = 0

    # again looking ahead one in my loop
    length = len(profit) - 1

    # Borrowing the same idea from my changes function above
    for i in range(length):
        this_month = int(profit[i])
        next_month = int(profit[i+1])
        change = next_month - this_month
        
        # now use an if statement to see if this change is greater than the last
        # and if so, store it in my great_date and great_change variables
        if change > great_change:
            great_date = date[i+1]
            great_change = change
    
    # the return is in the form of a dictionary with keys of month and change
    return {'month': great_date, 'change': great_change}

# finds the greatest decrease in losses (date and amount)
# over the entire period
# return will be in form of dictionary with keys of month and change
def great_dec(date,loss):

    # These are my place holders for greatset loss values
    great_date = ''
    great_change = 0

    # one more time I want a length that is one less then the length that i am puttin in
    length = len(loss) - 1

    # very similar to above but not quite (different variables and stuff)
    for i in range(length):
        this_month = int(loss[i])
        next_month = int(loss[i+1])
        change = next_month - this_month

        # again I will use a if statemanet but i will be looking for less then instead
        if change < great_change:
            great_date = date[i+1]
            great_change = change

    # the return again will be in the form of a dictionary. same keys to keep it simple:
    # month and change
    return {'month': great_date, 'change': great_change}


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

    # read rest of file into lists which will be put into dictonary
    for row in csvreader:
        finance[keys[0]].append(row[0])
        finance[keys[1]].append(row[1])

#----------------------------------------------------------------------
# use functions on dictionary to find desired values (and save them)

# find total months
tot_mon = len(finance[keys[0]])

# use sum_profit on dictionary
sum_prof = sum_profit(finance[keys[1]])

# use changes on dictionary
avg_change = changes(finance[keys[1]])

# use great_inc on dictionary
greater = great_inc(finance[keys[0]],finance[keys[1]])

# use great_dec on dictionary
lesser = great_dec(finance[keys[0]],finance[keys[1]])

# -----------------------------------------------------------------------------------------
# trying a new way to print and write to txt that is simpiler that Dom and Luis mentioned on slack
summary = (
            f'Financial Analysis\n'
            f'---------------------------------------\n'
            f'Total Months: {tot_mon}\n'
            f'Total: ${sum_prof}\n'
            f'Average Change: ${avg_change}\n'
            f'Greatest Increase in Profits: {greater["month"]} (${greater["change"]})\n'
            f'Greatest Decrease in Profits: {lesser["month"]} (${lesser["change"]})'
            )


#----------------------------------------------------------------------------------
# print summary of financial analysis
print(summary)

#---------------------------------------------------------------
# Write to txt file financial analysis
fin_ana = open('analysis/financial_analysis.txt', 'w')
fin_ana.write(summary)
fin_ana.close()
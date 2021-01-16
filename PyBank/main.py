## Andy McRae
## PyBank

# This script analyzes finacial records for my company

# import modules
import os
import csv


























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
    
    # ---------------------------------------------------------------------
    # old way of creating dictionary. turns out it just wasn't working 
    # because of a typo.

    # # read rest of file into lists which will be put into dictonary
    # date_list = []
    # profit_list = []

    # for row in csvreader:
    #     date_list.append(row[0])
    #     profit_list.append(row[1])

    # # creating dictionary with headers as keys
    # # keys[0] = 'Date' , keys[1] = 'Profit/Losses'
    # finance = {}
    # finance[keys[0]] = date_list
    # finance[keys[1]] = profit_list
    # # print(finance)

    # print(finance['Date'][1])
    # ---------------------------------------------------

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
    
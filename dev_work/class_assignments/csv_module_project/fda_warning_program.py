import csv

warning_letter = '483_2020.csv'

with open(warning_letter) as csv_file:
 
        # reading the csv file using DictReader
    csv_reader = csv.DictReader(csv_file)
 
    # converting the file to dictionary
    # by first converting to list
    # and then converting the list to dict
    dict_from_csv = dict(list(csv_reader)[0])
 
    # making a list from the keys of the dict
    list_of_column_names = list(dict_from_csv.keys())
 
    # displaying the list of column names
    print(list_of_column_names)
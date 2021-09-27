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
    
    #display column title by index
    posted_date = list_of_column_names[0]
    letter_sent = list_of_column_names[1]
    company_name = list_of_column_names[2]
    issuing_office = list_of_column_names[3]
    subject = list_of_column_names[4]
    response_letter = list_of_column_names[5]
    close_out = list_of_column_names[5]

    # displaying the list of column names
    print(f'{posted_date:>0}{company_name:>18} {issuing_office:>22} {subject:>19} {response_letter:>25}')
    print("-----------      ------------         --------------     ------------------------  ---------------")

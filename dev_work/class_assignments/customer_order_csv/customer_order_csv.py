#Feature 1
#create a csv file of different customer orders where each row contains a 
#       customer order along with customer name address and phone number
#after you have built that out you will create a function to change the name, and for extra credit (because some customers change the phone numbers) add in a way to modify the phone number
#you are writing this from scratch so no outside libraries

import csv
import os

mydict = [{'Sales Order ID': '0001','Product':'Tree Tea Oil','Customer ID':'35', 'Company Name':'Young Living ', 'Contact Name':'Aaron', 'Company Address': '', 'Phone Number':''}]

fields = ['Sales Order ID','Product','Customer ID', 'Company Name', 'Contact Name', 'Company Address', 'Phone Number']

filename = 'company_sales_order2021.csv'

with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fields)
    writer.writeheader()
    writer.writerows(mydict)

def clear_console():
    # Clear the console
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def open_list(filename, list):
    try:
        with open(filename) as file:
            data = file.read().splitlines()
            list.extend(data)
    except FileNotFoundError:
        pass


def show_option():
    clear_console()
    # Print out instructions on how to use the app
    print('')
    print('='*30)
    print('Customer Orders')
    print('='*30)
    print('')
    print("""
You have {} items in your list. \n
Enter O to show options.
Enter P to see your list.
Enter S to save your list
Enter R to remove an item.
Enter C to clear your list.
Enter QUIT to exit without saving.""".format(len(list)))

while True:
    new_item = input("\nAdd an item: ")
    if new_item == "q":
        show_list(sl)
        print("\nHave a nice day!\n")
        break
    elif new_item == "o":
        show_help(sl)
        continue
    elif new_item == "p":
        show_list(sl)
        continue
    elif new_item == "s":
        show_list(sl)
        save_list(saved_file, sl)
        break
    elif new_item == "c":
        delete_list(saved_file, sl)
        continue
    elif new_item == "REMOVE":
        remove_from_list(sl)
        continue
    else:
        add_to_list(new_item, sl)

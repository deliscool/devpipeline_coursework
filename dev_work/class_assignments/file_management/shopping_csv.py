import csv

fields = ['Name', 'Address', 'Phone', 'Order']
lines = []

def header_row():
    with open("shopping_csv.csv", "w",newline='') as shopping:
        wrt = csv.writer(shopping)
        wrt.writerow(fields)

def customer_info():
    name_1 = input("Enter your first and last name: ")
    address_1 = input("Enter your address: ")
    phone_1 = input("Enter your phone number: ")
    order_1 = input("What are you ordering today? ")
    rows = [name_1, address_1, phone_1, order_1]

    return rows

def create_user():
    with open('shopping_csv.csv', 'a', newline='') as outfile:
        wrt = csv.writer(outfile)
        wrt.writerow(customer_info())



def update_name():
        with open('shopping_csv.csv', 'rt') as outfile:
            csvreader = csv.reader(outfile)
            search = input('Enter your old name: ')
            new_name = input('What is your new name? ')
            for row in csvreader:                             
                if search not in row:
                    lines.append(row)
                if search in row:
                    replacment_name = [new_name,row[1],row[2],row[3]]
                    print(replacment_name)
        with open("shopping_csv.csv", "w",newline='') as outfile:
            wrt = csv.writer(outfile)
            header_row()
            wrt.writerows(lines)
            wrt.writerow(replacment_name)

def start_shopping():
    while True:
        menu = input('''Welcome to our shopping CSV!
    (C)reate Order
    (U)pdate Name
    (Q)uit
        ''').upper()

        if menu == 'C':
            create_user()
        elif menu == 'U':
            update_name()
        elif menu == "Q":
            print("Good Bye")
            break
        else:
            pass
        
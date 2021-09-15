#Python Bank Program
#Requirements: Check (B)alance ,Make a (D)eposit (W)ithdraw money (Q)uit
#Create a function for each of the first three options above.
#Bonus Make sure you are formatting your dollar amounts with only two decimal places, like $45.56, $89.00 etc
#Extra Bonus Error check the inputs when making deposits and withdrawals.

customer_login = False
customer_quit = False

customer = {
    'name':'',
    'balance': 550.00
}

#Initailizer
def create_customer():
    name = input('Enter your name:')
    customer["name"] = name
    global customer_login
    customer_login = True

# Options presentended
def start_bank():
    while customer_quit == False:
        if customer_login == False:
            print('Create account: ')
            create_customer
        else :
            print(f'{customer["name"]} Welcome! What would you like to do')
            response = input('Press w for withdraw  d to deposit and b to show your balance : ')
            if response == 'w':
                withdraw_money()
            elif response == 'd':
                deposit_money()
            elif response == 'b':
                check_balance()
            elif response == 'q':
                break
            else:
                print('Enter a correct value from given options')
start_bank()

# Function to check balance
def check_balance():
    print(f'Your balance is {customer["balance"]}')
    print('')


# Function to Deposit
def deposit_money():
    try:
        d_amount = int(input('How much money you want to deposit : '))
        customer['balance'] = customer['balance'] + d_amount
        print(f'{d_amount} has been deposited to your account your total balance is {customer["balance"]}')
        print('')
    except:
        print('Please enter a number')

# Function to withdraw the amount
def withdraw_money():
    try:
        w_amount = int(input('How much money you want to withdraw : '))
        if w_amount > customer['balance']:
            print('Your account does not have that much money')
        elif w_amount == 0:
            print('What you are fooling around here')
        else:
            customer['balance'] = customer['balance'] - w_amount
            print(f'{w_amount} has been withrawn from your account your total balance left is {customer["balance"]}')
            print('')
    except:
        print('Please enter a number')

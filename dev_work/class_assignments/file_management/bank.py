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
    name = input('Please your name:')
    customer['name'] = name
    global customer_login
    customer_login = True

# Function to check balance
def check_balance():
    print(f'Your balance is {customer["balance:2fr"]}')
    print('')


# Function to Deposit
def deposit_money():
    try:
        d_amount = int(input('How much money you want to deposit : '))
        customer['balance:fr'] = customer['balance:2fr'] + d_amount
        print(f'{d_amount} has been deposited to your account your total balance is {customer["balance:2fr"]}')
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
            print('You have no money in the bank.')
        else:
            customer['balance'] = customer['balance'] - w_amount
            print(f'{w_amount} has been withrawn from your account your total balance left is {customer["balance"]}')
            print('')
    except:
        print('Please enter a number')

#Options presented
def start_bank():
    while customer_quit == False:
        if customer_login == False:
            print('***=== Money Bank Front ===***')
            create_customer()
        else :
            print(f'Hello {customer["name"]}! What would you like to do?')
            response = str(input('Here are your options: \n(W) to withdraw  \n(D) to deposit \n(B) to show your balance \n(Q) to quit the program \n'))
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
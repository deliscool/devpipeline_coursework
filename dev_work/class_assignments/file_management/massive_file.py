import game_escape_room
import magic_eightball
import shopping_csv
import bank

user_login = False
user_quit = False

user = {
    'name':'',
}

def create_usern():
    user_n =input('Welcome to your program\n\nWhat is your name: ')
    user['name'] = user_n
    global user_login
    user_login = True

def program_start():
    while user_quit == False:
        if user_login == False:
            print('******** ==== Welcome to your Desktop === ********')
            print()
            create_usern()
        else:
            print('--------------------------------------')
            print(f'{user["name"]}, here are your programs')
            start_response = str(input('Options:\n(E)scape room \n(M)agic Eight Ball \n(S)hopping \n(B)ank \n(Q)uit '))
            answer = start_response.upper()
            if answer == 'E':
                game_escape_room.game_start()
            elif answer == 'M':
               magic_eightball.magic_eight_start() 
            elif answer == 'S':
                shopping_csv.start_shopping() 
            elif answer == 'B':
                bank.start_bank() 
            elif answer == 'Q':
                exit()
            else:
                print("Please input the following: \n(E)scape room \n(M)agic Eight Ball \n(S)hopping \n(B)ank")
                continue
program_start()
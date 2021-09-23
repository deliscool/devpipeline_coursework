from simple_chalk import chalk, green
import emoji

player_login = False
player_quit = False

player = {
    'name':'',
}

#Intializer of the game, name request
def create_usern():
    user_n =input('......You entered the escape room! \n\nWhat is your name: ')

    player['name'] = user_n
    global player_login
    player_login = True

#Start of game loop function
def game_play():
    while True:
        print(chalk.bgGreen(f'{player["name"]} in order to escape, try not to die. \nPlease choose from the following options:\n'))
        game_options = int(input('[1]Open the door? \n[2]Put hand in the hole? \n[3]Find key? \n'))
        if game_options == 2:
                print(chalk.red('You have died 😵!!!...again'))
                print(chalk.red('---------------------------'))
                continue
        elif game_options == 1:
                print(chalk.red('You do not have key 😫, try again'))
                print(chalk.red('---------------------------'))
                continue
        elif game_options == 3:
                print(chalk.blue('You found the key 😬!'))
                play_again()

#Play again function
def play_again():
  while True:
    again = str(chalk.bgBlue(input(f'{player["name"]} shall we play again?\n(Y) yes to play \n(Q) to quit')))
    if again == 'y':
      game_start()
    elif again == 'q':
      print('Game over! See you later 😬!')
      quit()
    else:
      print("Will only accept (Y) or (Q) inputs")
      continue
    
#Game introduction, yes or no options
def game_start():
    while player_quit == False:
        if player_login == False:
            print(green('******** ==== The Escape Room === ********'))
            print()
            create_usern()
        else:
            print(green('--------------------------------------'))
            print(chalk.red(f'Shall we play in the escaple room, {player["name"]}?'))
            start_response = str(input('Here are your options:\n(Y) yes to play \n(Q) to quit \n '))
            if start_response == 'y':
                game_play()
            elif start_response == 'q':
                print('Lets play next time. \n Game over!')
                quit()
            else:
                print("Will only accept (Y) or (Q) inputs")
                continue
game_start()
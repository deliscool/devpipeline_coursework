#This assignment will be to write a function that will return whether someone has won a game of tic-tac-toe.

def get_winner(board):
    for value in board:
        if value == 'x' or 'o':
            print ('Player has won!')
        elif value == '':
            print ('Neither player has won')
        else:
            print ('Not enough information')


#'X', if the 'X' player has won
#'O', if the 'O' player has won
#'', if neither player has won
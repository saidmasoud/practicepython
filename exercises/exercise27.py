'''The game starts out with an empty game board like this:

game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]
The computer asks Player 1 (X) what their move is (in the format row,col), and say they type 1,3. Then the game would print out

game = [[0, 0, X],
	[0, 0, 0],
	[0, 0, 0]]
And ask Player 2 for their move, printing an O in that place.

Things to note:

For this exercise, assume that player 1 (the first player to move) will always be X and player 2 (the second player) will always be O.
Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0). To people who don’t program, starting to count at 0 is a strange concept, so it is better for the user experience if the row counts and column counts start at 1. This is not required, but whichever way you choose to implement this, it should be explained to the player.
Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number. Then you can use your Python skills to figure out which row and column they want their piece to be in.
Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position where there already is another piece, do not allow the piece to go there.
Bonus:

For the “standard” exercise, don’t worry about “ending” the game - no need to keep track of how many squares are full. In a bonus version, keep track of how many squares are full and automatically stop asking for moves when there are no more valid moves.'''

# keep track of the number of open spaces remaining
open_spaces = 9
board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

def play_again():
    again = input("Want to play again?")
    return (True if again.lower()=='yes' else False)

def print_board(board):
    for row in board:
        print(row)

def check_for_winner(board, player):
    winner = False
    # Print if there is a row winner
    for row in board:
        if row[0] == row[1] and row[1] == row[2] and row[0]!=0:
            print("We have a row winner, player {}!".format(player))
            print_board(board)
            winner=True

    # Print if there is a column winner
    for i in range(0, 3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i]!=0:
            print('We have a column winner, player {}!'.format(player))
            print_board(board)
            winner = True

    # Print if there is a diagonal winner
    middle_mark = board[1][1]
    if(middle_mark!=0):
        if (board[0][0] == middle_mark and board[2][2] == middle_mark):
            print('We have a diagonal winner, left to right, player {}!'.format(player))
            print_board(board)
            winner = True
        elif (board[2][0] == middle_mark and board[0][2] == middle_mark):
            print("We have a diagonal winner, right to left, player {}!".format(player))
            print(board)
            winner = True
    return winner

def play(board):
    global open_spaces
    player = 1
    while(open_spaces>0):
        coord = input("Player {}, enter your choice: \n".format(player))
        split = coord.split(',')
        row = int(split[0])
        column = int(split[1])

        if(board[row][column]!=0):
            print("That space is already full!")
            print_board()
        else:
            board[row][column] = 'x' if player==1 else 'o'
            if(check_for_winner(board)==True):
                open_spaces = (9 if play_again() else 0)
            else:
                print("Here's the new board: ")
                print_board(board)
            # flip the player indicator after each turn successfully taken
            player = (1 if player==2 else 2)
            open_spaces-=1
        if(open_spaces==0 and check_for_winner(board)==False):
            print("Nobody won, it's a draw.")
            open_spaces = (9 if play_again() else 0)

    print("Thanks for playing!!!!!")

play(board)
# If a game of Tic Tac Toe is represented as a list of lists, like so:

# game = [[1, 2, 0],
#	[2, 1, 0],
#	[2, 1, 1]]
# where a 0 means an empty square, a 1 means that player 1 put their token in that space,
# and a 2 means that player 2 put their token in that space.

# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
# tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row -
# either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won -
# assume that in every board there will only be one winner.

def print_board(board):
    for row in board:
        print(row)

def check_for_winner(board):

    # Print if there is a row winner
    for row in board:
        if row[0] == row[1] and row[1] == row[2] and row[0]>0:
            print("We have a row winner!")
            print_board(board)

    # Print if there is a column winner
    for i in range(0, 3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i]>0:
            print('We have a column winner!')
            print_board(board)

    # Print if there is a diagonal winner
    middle_mark = board[1][1]
    if(middle_mark>0):
        if (board[0][0] == middle_mark and board[2][2] == middle_mark):
            print("We have a diagonal winner, left to right!")
            print_board(board)
        elif (board[2][0] == middle_mark and board[0][2] == middle_mark):
            print("We have a diagonal winner, right to left!")
            print(board)

# Create a two-dimensional list to represent the Tic-Tac-Toe board
board = [[1, 2, 0],[2, 1, 0],[2, 1, 1]]
check_for_winner(board)
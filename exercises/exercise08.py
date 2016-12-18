#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new game)

#Remember the rules:

#Rock beats scissors
#Scissors beats paper
#Paper beats rock
import sys

moves = ['rock','paper','scissors']

def game():
    move1 = input("Player 1, enter your move:")
    move2 = input("Player 2, enter your move:")

    if(move1 not in moves):
        print("Error: player 1 did not enter a valid move. Valid moves:",moves,". Exiting")
        sys.exit(1)
    elif(move2 not in moves):
        print("Error: player 2 did not enter a valid move, failing")
        sys.exit(1)

    if(move1==move2):
        print("It;s a tie! Both players entered",move1)
    elif(move1=='rock'):
        if move2=='paper':
            print('Congrats player 2, you win!')
        elif move2=='scissors':
            print('Congrats player 1, you win!')
    elif (move1 == 'paper'):
        if move2 == 'rock':
            print('Congrats player 1, you win!')
        elif move2 == 'scissors':
            print('Congrats player 2, you win!')
    elif (move1 == 'scissors'):
        if move2 == 'paper':
            print('Congrats player 1, you win!')
        elif move2 == 'rock':
            print('Congrats player 2, you win!')
    play_again = input("Play again? Enter 'yes' to play again")
    if(play_again=='yes'):
        game()

game()
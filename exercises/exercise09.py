#Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)

#Extras:

#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.
from random import randint

rand = randint(1,9)
count = 0
done = False
while(not done):
    count+=1
    guess = int(input("Guess a number between 0 and 9: "))
    if(guess==rand):
        print("You nailed it!!! Exiting")
        done = True
    elif(guess>rand):
        print("You guessed higher....")
    elif(guess<rand):
        print("You guessed lower...")
    if(not done):
        again = input("Play again??? Enter 'yes' to play again ")
        if(not again=='yes'):
            done = True
print(count,'guess(es) were taken')
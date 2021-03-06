#Create a program that will play the “cows and bulls” game with the user. The game works like this:

#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user
# guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the
# wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes
# throughout teh game and tell the user at the end.

#Say the number generated by the computer is 1038. An example interaction could look like this:

#  Welcome to the Cows and Bulls Game!
#  Enter a number:
#  >>> 1234
#  2 cows, 0 bulls
#  >>> 1256
#  1 cow, 1 bull
#  ...
#Until the user guesses the number.

import random

def main():
    print("Welcome to the Cows and Bulls Game!")
    number = str(random.randint(1000,9999))
    print("The password is:",number)
    guess = 0
    count = 0
    while(not guess==number):
        count+=1
        #assumes user entered four-digit number, no error handling
        guess = input("Enter a number: ")
        cows = 0
        bulls = 0
        for i in range(0,3):
            if(guess[i]==number[i]):
                cows+=1
            elif(guess[i] in number):
                bulls+=1
        if(guess==number):
            print("You got it!!! It took you",count,"guesses to get it right")
        else:
            print(cows,"cow(s),",bulls,"bull(s)")

main()
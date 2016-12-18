#In a previous exercise (exercise09.py), we’ve written a program that “knows” a number and asks a user to guess it.

#This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100.
#The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

#At the end of this exchange, your program should print out how many guesses it took to get your number.

#As the writer of this program, you will have to choose how your program will strategically guess.
# A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number.
# But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50
# (right in the middle of the range), and then increase / decrease by 1 as needed. After you’ve written the program,
# try to find the optimal strategy!

#Use binary search. Reusing code form exercise20

import math

tries = 0
list = [a for a in range(1,101)]


def guess_num(list):
    if(len(list)==1):
        result = ask(list[0])
        if(result == 0):
            return
        else:
            print("We Failed :(")
            return

    # we subtract 1 because the index starts at zero, and take the ceiling because, for example, a list of 3 would
    # result in midpoint being zero
    midpoint = math.ceil((len(list)/2))-1
    result = ask(list[midpoint])
    cut_list = []
    if(result==0):
        return
    elif(result==1):
        cut_list = list[:midpoint]
    else:
        cut_list = list[midpoint:]
    # use recursion to keep cutting down the list until
    # only one element remains
    return guess_num(cut_list)

# returns:
#   *0 if guess was correct
#   *-1 if guess was too low
#   *1 if guess was too high
def ask(number):
    global tries
    tries+=1
    response = input("Is {} your number? ".format(number))
    if response=="yes":
        print("Yesssssss!!!!!!!!! Only took {} tries :) ".format(tries))
        return 0
    else:
        response = input("Was that guess too high or too low?")
        if response == "low":
            return -1
        else:
            return 1

guess_num(list)
'''In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses
(head, body, 2 legs, and 2 arms) before they lose the game.

In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the letter
and displaying that information to the user. In this exercise, we have to put it all together and add logic
for handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:

* Only let the user guess 6 times, and tell the user how many guesses they have left.
* Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them -
  let them guess again.
Optional additions:

* When the player wins or loses, let them start a new game.
* Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman.
  This is challenging - do the other parts of the exercise first!'''

def play(word):
    print('Welcome to Hangman!')
    # the word split into different letters
    letter_list = list(word)
    # the list to be printed after each guess
    print_list = ['-'] * len(word)
    # keeping track of letters guesses
    guess_list = []
    # keeping track of number of guesses
    counter = 0

    # keep guessing until word is guessed
    while '-' in print_list:
        counter+=1
        guess = input('Guess your letter: ').upper()
        if guess in guess_list:
            print("You already guessed that letter:")
            print_hangman(print_list)
            counter-=1
        elif guess not in letter_list:
            print("Incorrect!")
            print_hangman(print_list)
        else:
            for i in range(len(letter_list)):
                if letter_list[i]==guess:
                    print_list[i]=guess
            if '-' not in print_list:
                print("You won!!! It only took you {} guesses".format(counter))
                return
            print_hangman(print_list)
            counter-=1
        if(counter==6):
            print("Sorry, you ran out of guesses! You Lose.")
            return
        else:
            print("You have {} many guesses left...".format(6-counter))



def print_hangman(list):
    str = ''
    for i in list:
        str+=i
    print (str)

def play_again():
    choice = input('Want to play again?').lower()
    if(choice=='yes' or choice=='y'):
        word = input('Great! What word do you want to play with?')


play("EVAPORATE")

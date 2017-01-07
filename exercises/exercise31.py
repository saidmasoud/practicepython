'''Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to
guess, letter by letter. The player guesses one letter at a time until the entire word has been guessed.
(In the actual game, the player can only guess 6 letters incorrectly before losing).

Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player
to guess a letter and displays letters in the clue word that were guessed correctly. For now, let the player guess
an infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed
and display a different message if the player tries to guess that letter again. Remember to stop the game when all
the letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number
of guesses the player has remaining - we will deal with those in a future exercise.

An example interaction can look like this:

Welcome to Hangman!
_ _ _ _ _ _ _ _ _
Guess your letter: S
Incorrect!
Guess your letter: E
E _ _ _ _ _ _ _ E
...
And so on, until the player gets the word.'''

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
        elif guess not in letter_list:
            print("Incorrect!")
            print_hangman(print_list)
        else:
            for i in range(len(letter_list)):
                if letter_list[i]==guess:
                    print_list[i]=guess
            if '-' not in print_list:
                print("You won!!! It only took you {} guesses".format(counter))
            print_hangman(print_list)



def print_hangman(list):
    str = ''
    for i in list:
        str+=i
    print (str)

play("EVAPORATE")
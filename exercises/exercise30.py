'''In this exercise, the task is to write a function that picks a random word from a list of words from the
SOWPODS dictionary. Download this file and save it in the same directory as your Python code.
This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments.
Each line in the file contains a single word.'''
import random

def random_sowpods(filename):
    list = []
    with open(filename) as file:
        for line in file:
            list.append(line.replace('\n',''))
    file.close()
    return list[random.randint(0,len(list)-1)]

print (random_sowpods('sowpods.txt'))
#Write a function that takes an ordered list of numbers (a list where the elements are in order
# from smallest to largest) and another number. The function decides whether or not the given number is inside the
# list and returns (then prints) an appropriate boolean.

#Extras:

#Use binary search.

import math

def in_list(list,number):
    if(len(list)==1):
        if(list[0]==number):
            return True
        else:
            return False
    # had to put this in because of RecursionError when checking for 500 in below example list
    elif(len(list)==2):
        if(list[0]>number or list[1]<number):
            return False
        else:
            return in_list([list[0]],number) or in_list([list[1]],number)
    # we subtract 1 because the index starts at zero, and take the ceiling because, for example, a list of 3 would
    # result in midpoint being zero
    midpoint = math.ceil((len(list)/2))-1
    cut_list = []
    if(list[midpoint]==number):
        return True
    elif(list[midpoint]>number):
        cut_list = list[:midpoint]
    else:
        cut_list = list[midpoint:]
    # use recursion to keep cutting down the list until
    # only one element remains
    return in_list(cut_list,number)

list = [1, 3, 5, 30, 31, 42, 43, 500]

print(in_list(list,1))

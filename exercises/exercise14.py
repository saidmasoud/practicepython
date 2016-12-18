#Write a program (function!) that takes a list and returns a new list that contains all the elements of the
# first list minus all the duplicates.

#Extras:

##Write two different functions to do this - one using a loop and constructing a list, and another using sets.
##Go back and do Exercise 5 using sets, and write the solution for that in a different function.

def unique_list(list):
    unique = []
    for i in list:
        if i not in unique:
            unique.append(i)
    return unique

def unique_set(list):
    return set(list)

list = [5,5,10,10]

print(unique_list(list))
print(unique_set(list))
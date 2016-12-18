#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Extras:

#Add on to the previous program by asking the user for another number and
#printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines.
#(Hint: the string "\n is the same as pressing the ENTER button)

import sys

name = input("What's your name? ")
try:
    age = int(input("What's your age? "))
except ValueError:
    print("Please enter digits only when entering in your age.")
    #quit()
    sys.exit(1)

if(age>=100):
    print("You're already at least a hundred years old! Wow!")
elif(age<1):
    print("Invalid age >:(")
else:
    difference = 100-age
    print("Thanks",name,"!!! It will take you",difference,"years to become 100 years old.")
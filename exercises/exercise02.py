#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message
# to the user. Hint: how does an even / odd number react differently when divided by 2?

#Extras:

#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

import sys

try:
    num = int(input("What number would you like to check?"))
    check = int(input("What number would you like to divide by?"))
except ValueError:
    print("Invalid number, exiting")
    sys.exit(1)

if(num%4==0):
    print(num,"divides evenly into 4!!!")
elif(num%2==0):
    print(num,"appears to be an even number")
else:
    print(num, "appears to be an odd number")

if(num%check==0):
    print(check,"divides evenly into",num)
else:
    print(check, "does not divides evenly into", num)
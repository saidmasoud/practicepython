#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
import sys

try:
    num = int(input("Enter a number: "))
    divisors = []
    for divisor in range(num):
        if(divisor==0):
            pass
        elif(num%divisor==0):
            divisors.append(divisor)
    print(divisors)
except ValueError:
    print("Invalid number, failing")
    sys.exit(1)


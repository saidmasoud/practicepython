#Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

str = input("Let's have a string, shall we?")

palindrome = str[::-1]==str
if palindrome:
    print(str,"is a palindrome")
else:
    print(str, "is not a palindrome")
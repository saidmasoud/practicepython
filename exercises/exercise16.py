#Write a password generator in Python. Be creative with how you generate passwords -
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

#Extra:

#Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import ast, random

def main():
    #password to be printed
    password = ''

    strong = input("Do you want a strong password?")

    if(not strong.lower()=='yes'):
        list = ["SumPass", "AKewlPass","ofdijsdf"]
        password = list[random.randrange(0,2)]
    else:
        #random ASCII value for lowercase letters
        lower = chr(random.randrange(97,122))
        # random ASCII value for uppercase letters
        upper = chr(random.randrange(65, 90))
        # random ASCII value for symbols
        symbol = chr(random.randrange(33, 46))
        # random ASCII value for numbers
        number = random.randrange(0, 999999)

        password = lower+upper+symbol+str(number)
    print("Your generated password is: ",password)

main()
#Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to [Exercise 4](/exercise/2014/02/26/04-divisors.html to help you.
# Take this opportunity to practice using functions, described below.


def divisors(num):
    divisor_list = []
    for divisor in range(num+1):
        if (divisor == 0):
            pass
        elif (num % divisor == 0):
            divisor_list.append(divisor)
    return divisor_list

num = int(input("Enter a number: "))
print(divisors(num))
if(len(divisors(num))<=2):
    print(num,"is prime")
else:
    print(num,"is not prime")
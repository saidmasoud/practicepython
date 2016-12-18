# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the
# number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers
# where the next number in the sequence is the sum of the previous two numbers in the sequence.
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

numbers = int(input("Enter Fibonacct number: "))
sequence = []
for num in range(numbers+1):
    if num==0:
        pass
    else:
        sequence.append(fib(num))
print(sequence)
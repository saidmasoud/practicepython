#Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file (http://www.practicepython.org/assets/primenumbers.txt) has a list of all prime numbers under 1000, and
# the other .txt file (http://www.practicepython.org/assets/happynumbers.txt) has a list of happy numbers up to 1000.

prime_list = []
overlap = []
with open('primenumbers.txt') as prime_file:
    for line in prime_file:
        number = int(line.replace('\n',''))
        prime_list.append(number)

with open('happynumbers.txt') as happy_file:
    for line in happy_file:
        number = int(line.replace('\n', ''))
        if number in prime_list:
            overlap.append(number)

print(overlap)
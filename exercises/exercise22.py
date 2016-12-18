# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,
# and print out the results to the screen. I have a .txt file for you, if you want to use it!
# http://www.practicepython.org/assets/nameslist.txt

#Extra:

# Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file,
# http://www.practicepython.org/assets/Training_01.txt
# and count how many of each “category” of each image there are. This text file is actually a list of files
# corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images.
# Once you take a look at the first line or two of the file, it will be clear which part represents the scene category.
# To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it
# in this post. -> http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

# main task
def part1():
    dict = {}
    with open('namelist.txt') as file:
        for line in file:
            # remove the newline character
            name = line.replace('\n','')
            try:
                dict[name]+=1
            except KeyError:
                dict[name]=1
    print(dict)

part1()

# extra task
def part2():
    dict = {}
    with open('imagelist.txt') as file:
        for line in file:
            # remove the newline character and split by backslash
            split = line.replace('\n','').split('/')
            letter = split[1]
            category = split[2]
            if letter in dict:
                try:
                    dict[letter][category]+=1
                except KeyError:
                    dict[letter][category]=1
            else:
                dict[letter]={category:1}
    for letter in sorted(dict.keys()):
        print(letter,": \n",dict[letter])

part2()
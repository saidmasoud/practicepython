#Time for some fake graphics! Let’s say we want to draw game boards that look like this:

# --- --- ---
#|   |   |   |
# --- --- ---
#|   |   |   |
# --- --- ---
#|   |   |   |
# --- --- ---
#This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes
# (8x8 for chess, 19x19 for Go, and many more).

# Ask the user what size game board they want to draw,
# and draw it for them to the screen using Python’s print statement.

# ASSUMPTION: printing a square game board
# -Said

size = int(input("What size do you want the game board to be? "))

# build top border
border = ""
for i in range(0,size):
    border+=" ---"

# build row
row_edges = ''
row_floors = ''
for i in range(0,size):
    row_edges += '|   '
    row_floors += ' ---'

# print board
print(border)
for i in range(0,size):
    print(row_edges+'|')
    print(row_floors)
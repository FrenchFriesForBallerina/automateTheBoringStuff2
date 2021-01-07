# this function needs to check if a given dictionary of board pieces layout is valid.
# this means: 1- the key values can only be the 64 squares and used by only one piece at a time.
# 2 - there can only be a max number of pieces for both white and black.
# 3 - the color of a piece can only be either black or white.

# also, the function should recognize if the board is faulty and give a warning.

# so there should be a tuple of valid squares, and a dictionary of all the pieces one player can have

# the board is checked as following:
# all of the keys are checked for 2 things: 1 - are they all valid, 2 - do they all appear just once
# in the dictionary. If they do, the values (pieces) are checked.

# the pieces are checked in a following way:
# the number of occurence of each piece is checked with accordance with the dictionary of all the pieces.
# if the number of the pieces does not exceed the max number, then they are valid too.

#def isValidChessBoard(takeDictionary):
    #function in here

# so here is a loop to create all valid chess squares:

import pprint

chessLetters = ['a','b','c','d','e','f','g','h']
chessSquares = []
number = 1
for i in chessLetters:
    while number < 9:
        chessSquares.append(i + str(number))
        number += 1
    number = 1
tuple(chessSquares)

# here is the dictionary with all the pieces and their maximum number that one player can have:
pieces = {'bpawn': 8, 'bknight': 2, 'bbishop': 2, 'brook': 2, 'bking': 1, 'bqueen': 1, 'wpawn': 8, 'wknight': 2, 'wbishop': 2, 'wrook': 2, 'wking': 1, 'wqueen': 1}

# now a function needs to be written that takes a board as an argument and checks if the squares
# and the pieces are valid.

#message = 'It was a bright cold day in April, and the clocks were striking
#thirteen.'
#count = {}

#for character in message:
#➊ count.setdefault(character, 0)
#➋ count[character] = count[character] + 1

#print(count)

exampleBoard = {'1h': 'bking', '1h': 'wqueen', '1h': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

# go through keys in example board and see if they all appear just once in the dictionary

listOfSquares =
count = {}

for i in exampleBoard.keys():
    count.setdefault(i, 0)
    count[i] = count[i] + 1

pprint.pprint(count)

for i in count.values():
    print(i)
    if i > 1:
        print('invalid number of squares, board faulty')

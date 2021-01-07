chessLetters = ['a','b','c','d','e','f','g','h']
chessSquares = []
number = 1
for i in chessLetters:
    while number < 9:
        chessSquares.append(i + str(number))
        number += 1
    number = 1
print(chessSquares)
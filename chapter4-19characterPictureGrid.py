grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#x varies between -1 and -9 (-len(grid)), so x = -1, while x >= - len(grid), x -= 1
#y varies between 0 and 6 (len(grid[x])), so y = 0, while y < 6, y += 1

x = -1
y = 0

while y < 6:
    while x >= -len(grid):
        print(grid[x][y], end = '')
        x -= 1
    print()
    x = -1
    y += 1
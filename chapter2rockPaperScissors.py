import random, sys

wins = 0
losses = 0
ties = 0

print('ROCK, PAPER, SCISSORS')

answer = ''

while True:
    print(str(wins) +' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')
    answer = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit\n')

    if answer == 'q':
        sys.exit()
    computersAnswer = random.randint(1,3)

    if answer == 'r':
        print('ROCK versus...')
        answer = 1
    elif answer == 'p':
        print('PAPER versus...')
        answer = 2
    elif answer == 's':
        print('SCISSORS versus...')
        answer = 3
    else:
        print('Are you sure you typed in an available option?')
        continue

    if computersAnswer == 1:
        print('ROCK')
    if computersAnswer == 2:
        print('PAPER')
    if computersAnswer == 3:
        print('SCISSORS')

    if answer == computersAnswer:
        ties = ties + 1
        print('It is a tie!')
    elif answer == 2 and computersAnswer == 1:
        wins = wins + 1
        print('You win!')
    elif answer == 1 and computersAnswer == 3:
        wins = wins + 1
        print('You win!')
    elif answer == 3 and computersAnswer == 2:
        wins = wins + 1
        print('You win!')
    elif answer == 1 and computersAnswer == 2:
        losses = losses + 1
        print('You lose!')
    elif answer == 2 and computersAnswer == 3:
        losses = losses + 1
        print('You lose!')
    elif answer == 3 and computersAnswer == 1:
        losses = losses + 1
        print('You lose!')


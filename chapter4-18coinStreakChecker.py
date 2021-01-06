import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    options = ['H', 'T']
    listOfHeadsAndTails = []
    currentStreak = 0
    i = 0
    listOfHeadsAndTails.append(random.choice(options))
    while i < 100:
        listOfHeadsAndTails.append(random.choice(options))
        if listOfHeadsAndTails[i] == listOfHeadsAndTails[i - 1]:
            currentStreak += 1
        else:
            if currentStreak == 6:
                print('and another streak')
                numberOfStreaks += 1
            currentStreak = 0
        i += 1

        # Code that checks if there is a streak of 6 heads or tails in a row.


print(listOfHeadsAndTails)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
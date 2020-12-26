import random
number = random.randint(1,20)
guess = ''
counter = 0
print('I am thinking of a number between 1 and 20.')

while guess != number:
    counter = counter + 1
    print('Take a guess.')
    guess = int(input())

    if guess > number:
        print('Your guess is too high.')
        continue
    elif guess < number:
        print('Your guess is too low.')
        continue
    elif guess == number:
        print('Good job! You guessed my number in ' + str(counter) + ' guesses.')
        break
def collatz(number):

    if(number % 2 == 0):
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return (3 * number + 1)

userInput = int(input('Type in a number:\n'))
result = collatz(userInput)
while True:
    if collatz(result) != 1:
        result = collatz(result)
    else:
        print('the result is now 1')
        break
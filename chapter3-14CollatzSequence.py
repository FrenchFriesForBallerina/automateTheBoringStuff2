def collatz(number):

    if(number % 2 == 0):
        value = number // 2
        print(value)
        return value

    else:
        value = 3 * number + 1
        print(value)
        return value

userInput = input('Type in a number:\n')
result = int(userInput)

while True:
    if result != 1:
        result = collatz(result)
    else:
        break

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
try:
    result = int(userInput)
except ValueError:
    while userInput.isnumeric() == False:
        userInput = input('No, a number, please:\n')

result = int(userInput)
while True:
    if result != 1:
        result = collatz(result)
    else:
        break

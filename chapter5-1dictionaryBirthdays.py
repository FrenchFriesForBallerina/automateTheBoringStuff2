birthdays = {'April':'Apr 1', 'Charlie': 'May 1', 'Edna': 'Dec 31'}

while True:
    print ('Enter a name: (blank to quit)')
    name = input().capitalize()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
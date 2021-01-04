myPets = ['Morris', 'Xena', 'Yaldis']
pet = input('Enter a pet name: ').capitalize()

if pet in myPets:
    print('I also have a pet named ' + pet + '!')
else:
    print('I do not have a pet named ' + pet)
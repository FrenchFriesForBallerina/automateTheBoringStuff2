import random
pets = ['dog', 'cat', 'pelican']
print(random.choice(pets))

#print a random pet a specified number of times
for i in range(9):
    print(random.choice(pets))

#randomly shuffle the order of pets in the list and print the new list
random.shuffle(pets)
print(pets)
catNames = []

for i in range(6):
    catNames = catNames +[input('Enter the name of cat ' + str(i + 1) + ' (Or enter nothing to stop.)\n')]
print('The cat names are:')
for i in range(len(catNames)):
    print(catNames[i])
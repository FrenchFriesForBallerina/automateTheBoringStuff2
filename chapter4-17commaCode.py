spam = ['apples', 'bananas', 'tofu', 'cats']

def commaCode(listValues):
    theStringOfValues = ''
    if listValues != []:
        for item in listValues:
            if listValues.index(item) != len(listValues)  - 1:
                theStringOfValues += str(item) + ', '
            else:
                theStringOfValues += 'and ' + str(item)

    else:
        print('The list is empty!')
    return theStringOfValues

print(commaCode(spam))
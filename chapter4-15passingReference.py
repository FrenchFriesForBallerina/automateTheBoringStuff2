def eggs(aParameter):
    aParameter.append('hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

#to compare, lets take a look at how trying
#to modify a string will not affect the value of a string:

def words(aParameter):
    aParameter = aParameter + ' and goodbye'
    print(aParameter)

word = 'hello'
words(word)
print(word)

#the string did not change, as it is immutable!
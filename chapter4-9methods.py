# a method is the same thing as a function,
#except it's 'called on' a value.
#each data type has its own set of methods.

spam = ['hello', 'goodbye', 'oh it is you again']
print(spam.index('goodbye'))
spam += ['hello']
print(spam)
print(spam.index('hello'))

#to add a value to the list, there are append() and insert() methods,
#although my += worked perfectly fine :) let's see how they work:

spam.append('lovely to see you')
print(spam)

spam.insert(0, 'ho ho ho')
print(spam)

#so it appears that append() adds the new value to the end of the list and insert() adds a new value at the
#chosen index, neither of them overwrites the existing values.

#it's interesting that methods belong to a single data type.
#The append() and insert() methods are list methods and can be called only on list values, not on
#other values such as strings or integers.
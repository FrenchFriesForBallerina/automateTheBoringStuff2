#importing random for later use
import random

#creating a list
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
#here where random is needed: to print out a random value from the list
print(random.choice(supplies))

#I want to do tuple unpacking. First, I convert the list supplies
#to a tuple with the same value, and print the value:
supplies = tuple(supplies)
print(supplies)

#here is an example of tuple unpacking:
write, connect, fight, bind = supplies
print(write)

#sequence data types are:
#lists
#strings
#range objects returned by range()
#tuples

#there are mutable and immutable data types.
#most Python objects are immutable.

#mutable data types are:
#lists
#dictionaries

#immutable data types are:
#strings (to mutate a string, use concatenation and slicing)
#booleans
#integers
#floats
#tuples

#functions to use with lists:
#append()
#insert()
#sort()
#remove()
#del
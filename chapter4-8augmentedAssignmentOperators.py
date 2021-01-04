spam = 54
#instead of this line:
#spam = spam + 1
#it's shorter to write:
spam += 1
print(spam)

#same stuff applies to other operators like +, -, *, /, and %

spam -= 1 # this does the same as spam = spam - 1:
print(spam)

spam *= 0.5
print(spam)

spam /= 9
print(int(spam))

spam %= 2
print(spam)

#what is cool is that two of these operators can be used to modify strings and lists.
#these operators are + and *. Here's how they work:

print('Here is how operators + and * work:')
hello = 'Hello, '
print(hello)
print('And now some magic with + and *!')

hello += 'everyone! '
print(hello)
hello *= 3
print(hello)
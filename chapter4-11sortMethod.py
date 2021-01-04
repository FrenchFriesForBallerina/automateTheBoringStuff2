spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

spam = ['.','*',',','2', 'ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)

spam.remove('.')
spam.remove('2')
spam.remove('*')
spam.remove(',')
print(spam)

spam.sort(reverse = True)
print(spam)

#it's interesting
#that sort() uses
#“ASCIIbetical order” rather than actual alphabetical
#order for sorting strings. This means uppercase letters
#come before lowercase letters.
#so to sort the values in regular alphabetical order,
#one should pass str.lower() for the key keyword argument
#in the sort() method call.

spam = ['A', 'z', 'a', 'Z']
print(spam)
spam.sort(key = str.lower)
print(spam)
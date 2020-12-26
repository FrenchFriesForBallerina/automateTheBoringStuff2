while True:
    name = input('Who are you?\n')
    if name != 'joe':
        continue
    print('hello joe. What is the password? (it is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted')
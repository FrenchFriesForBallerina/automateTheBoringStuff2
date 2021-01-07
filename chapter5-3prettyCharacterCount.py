import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
#if you want to obtain the prettified text as a string value instead of displaying it on the screen, call pprint.pformat() instead.
print(pprint.pformat(count))
import time, sys

indent = ' '
asteriscs = '********'
i = 5

while True:

    while i >= 0:
        print(indent * i + asteriscs)
        i = i - 1
        time.sleep(0.5)
    i = i + 2
    while i <= 4:
        print(indent * i + asteriscs)
        i = i + 1
        time.sleep(0.5)
    i = i - 2
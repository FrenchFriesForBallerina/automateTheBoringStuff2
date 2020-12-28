import time, sys
indent = 0
indentIncreasing = True

try:
    while True:
        print(' '*indent, end = '')
        print('********')
        time.sleep(0.5)

        if indentIncreasing:
            indent = indent + 1
            if indent == 5:SS
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()

emailFile = open('emails.txt', 'r')

emails = emailFile.readlines()
cleanEmails = []
a = ''
for i in emails:
    a = i.replace('\n', '')
    cleanEmails.append(a)

cleanEmails = list(dict.fromkeys(cleanEmails))
print(cleanEmails)
print(len(cleanEmails))

theListToUse = ''

for i in cleanEmails:
    if cleanEmails.index(i) != len(cleanEmails) - 1:
        theListToUse += i + ', '
    else:
        theListToUse += i + ''

print(theListToUse)

f = open('emailsToSendTo.txt', 'w')
f.write(theListToUse)
f.close()
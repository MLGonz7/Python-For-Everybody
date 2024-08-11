import re

handle = open('practice.txt', 'r')
numlist = list()
for line in handle:
    num = re.findall('[0-9]+',line)
    numlist = numlist + num

sum = 0
for val in numlist:
    sum = sum + int(val)

print('Total:', sum)

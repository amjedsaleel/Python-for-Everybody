import re

x = 'my 2 favorite numbers are 19 and 42'
# y = re.findall('[0-9]+', x)
# print(y, '\n')

# z = re.findall('[AEIOU]+', x)
# print(z, '\n')


# greedy matching
a = 'From: Using the : character'
# print(re.findall('F.+:', a), '\n')


# non-greedy
# print(re.findall('^F.+?:', a), '\n')


# Fine- Tuning String extraction
c = 'From amjedsaleel@gmail.com Sat Jan 5 09:14:16 2020'
cc = re.findall('\S+@\S+', c)
print(cc)








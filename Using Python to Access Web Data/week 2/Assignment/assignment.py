import re

file = open('actual_regex_sum.txt')

sum = 0
words = 0
for line in file:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    if len(numbers) > 0:
        for number in numbers:
            words += 1
            sum += int(number)

print(words, sum)

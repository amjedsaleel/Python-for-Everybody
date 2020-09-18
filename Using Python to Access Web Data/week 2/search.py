import re

handle = open('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    # if re.search('From ', line):
    if re.search('^From ', line):
        print(line)

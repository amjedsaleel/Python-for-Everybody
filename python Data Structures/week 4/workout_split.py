mbox = open('mbox-short.txt')
for line in mbox:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])

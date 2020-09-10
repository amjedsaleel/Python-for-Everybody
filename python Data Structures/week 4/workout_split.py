mbox = open('mbox-short.txt')
# for line in mbox:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue
#     words = line.split()
#     print(words[2])


# double split
print('')
for line in mbox:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print('Words:', words)
    email = words[1]
    pieces = email.split('@')

    print('Email:', email)
    print('Pieces:', pieces)
    print('')
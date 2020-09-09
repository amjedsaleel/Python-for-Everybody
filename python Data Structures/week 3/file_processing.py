files = open('file.txt')

# count = 0
# for file in files:
#     count = count + 1
#     print('Total line: ',count)
#     print(file)

# text = files.read()
# print(text)



# search

# for line in files:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)

# advance search

# for line in files:
#     line = line.rstrip()
#     if not line.startswith('From:'):
#         continue
#     print(line)



# select lines

for line in files:
    line = line.strip()
    if not '@uct.ac.za' in line:
        print(line)


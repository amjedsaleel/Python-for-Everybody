name = input('Enter file: ')
handle = open(name)

hours = list()
for line in handle:
    if line.startswith('From '):
        line = line.rstrip()
        word = line.split()
        # print(word)
        time = word[5].split(':')
        hour = time[0]
        hours.append(hour)

count = dict()
for hour in hours:
    count[hour] = count.get(hour, 0) + 1

lst = list()
for key, value in count.items():
    new_tuple = (key, value)
    lst.append(new_tuple)

lst = sorted(lst)

for key, value in lst:
    print(key, value)



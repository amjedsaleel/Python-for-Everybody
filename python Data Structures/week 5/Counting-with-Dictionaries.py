names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
count = dict()

for name in names:
    if name in count:
        count[name] = count[name] + 1
    else:
        count[name] = 1

print(count)
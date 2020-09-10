# fname = input("Enter file name: ")
fh = open('remeo.txt')
lst = list()
for line in fh:
    for word in line.split():
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print(lst)




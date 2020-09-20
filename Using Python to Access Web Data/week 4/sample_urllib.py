import urllib.request

# retrieve files and it print in console
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

count = dict()
for line in fhand:
    line = line.decode().strip()
    print(line)
print('\n')


# retrieving file and counts number of words word in that file
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    words = line.decode().split()
    # print(words)
    for word in words:
        count[word] = count.get(word, 0) + 1

for key, value in count.items():
    print(key, value)
print('\n')


# retrieving web pages
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

for line in fhand:
    line = line.decode().strip()
    print(line)
print('\n')
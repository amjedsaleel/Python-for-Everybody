import urllib.request
import re

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

for line in fhand:
    line = line.decode().strip()
    link = re.findall('[http]? ', line)
    print(link)
    # print(line)
print('\n')
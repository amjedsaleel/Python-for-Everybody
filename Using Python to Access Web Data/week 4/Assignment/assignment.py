import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore ssl error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve numbers
numbers = list()
tags = soup('span')
for tag in tags:
    numbers.append(tag.contents[0])

# Calculate total sum and count the total numbers from numbers list
sum = 0
for number in numbers:
    sum += int(number)

print(sum)
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
html = urllib.request.urlopen(address).read().decode()
print('Retrieving', address)

data = ET.fromstring(html)
tags = data.findall('comments/comment')

print('Retrieved', len(tags), 'characters')

count = 0
sum = 0
for tag in tags:
    count += 1
    sum += int(tag.find('count').text)
print('Count:', count)
print('Sum:', sum)


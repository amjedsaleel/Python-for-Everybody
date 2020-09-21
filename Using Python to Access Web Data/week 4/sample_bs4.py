import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm').read()
soup = BeautifulSoup(html, 'html.parser')

# retrieving all anger tage
tages = soup('a')
print(tages)
for tage in tages:
    print(tage.get('href', None))



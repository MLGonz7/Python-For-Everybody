# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
number = int(input('Enter number - '))
where = int(input('Enter position - '))

print('Retrieving: %s' % url)
for i in range(0, number):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    count = 0
    position = 0
    for tag in tags:
        position += 1
        if position == where:
            print('Retrieving: %s' % str(tag.get('href', None)))
            url = str(tag.get('href', None))
            position = 0
            break

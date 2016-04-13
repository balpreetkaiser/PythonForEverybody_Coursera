# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
#html = urllib.urlopen('http://python-data.dr-chuck.net/comments_221579.html').read()
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

total = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print 'TAG:',tag
    #print 'URL:',tag.get('href', None)
    total = total+int(tag.contents[0])
    #print 'Attrs:',tag.attrs
print total


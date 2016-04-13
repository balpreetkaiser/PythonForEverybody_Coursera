# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
link_pos=raw_input("Enter the number of times link position shoud be modified: ")
repeat_for = raw_input("Total numer of times the process should be repeated: ")
lp = int(link_pos)
tpr = int(repeat_for)
print url
for i in range(tpr):
    soup = BeautifulSoup(urllib.urlopen(url).read())
    tags = soup('a')
    url = tags[lp-1].get('href', None)
    print url


#html = urllib.urlopen(url).read()
#soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
 #   print tag.get('href', None)


import urllib
import xml.etree.ElementTree as ET

comentCount = 0
total = 0
url = raw_input('Enter location: ')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)

counts = tree.findall('.//count')

for items in counts:
    comentCount = comentCount+1
    total = total+int(items.text)
print "Count: ", comentCount
print "Sum: ",total

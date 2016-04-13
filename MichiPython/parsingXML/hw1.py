import urllib
import xml.etree.ElementTree as ET

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

url  = raw_input('Enter location: ')

   # url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    #print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data
tree = ET.fromstring(data)


counts = tree.findall('.//count')
for items in counts:
    print items


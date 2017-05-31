import urllib
import xml.etree.ElementTree as ET
link = raw_input('Enter website: ')
url = urllib.urlencode({'sensor':'false', 'address': link})
print 'Retrieving', url
uh = urllib.urlopen(link)
data = uh.read()
uh.close()

tree = ET.fromstring(data)
counts=tree.findall('.//count')
x=list()
for count in counts:
    y=int(count.text)
    x.append(y)


print sum(x)
# x=list()
# for result in results:
#     x=x+result.txt
#
# print x
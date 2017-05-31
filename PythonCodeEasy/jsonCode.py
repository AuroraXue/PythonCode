import urllib
import json
address=raw_input("Enter the website: ")
address1=urllib.urlopen(address)
address2=address1.read()
data=json.loads(str(address2))

x=list()
for item in data['comments']:
    x.append(item['count'])

x=map(int,x)
print sum(x)
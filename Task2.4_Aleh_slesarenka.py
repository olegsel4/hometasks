import re
from collections import Counter

f=open('access.log')
data = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', f.read())
f.close()
for address in Counter(data).most_common(5):
   print (address[0])
import xml.etree.ElementTree as ET
from urllib.request import urlopen
url = urlopen("https://py4e-data.dr-chuck.net/comments_1961950.xml")
tree = ET.fromstring(url.read())
process = tree.findall('comments/comment')
sum = 0
for i in process:
    sum += int(i.find('count').text)
print(sum)
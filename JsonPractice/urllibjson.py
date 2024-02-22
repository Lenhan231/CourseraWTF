from urllib.request import urlopen
import json
url = urlopen("https://py4e-data.dr-chuck.net/comments_1961951.json")
info = json.load(url)
sum = 0 
for item in info['comments']:
    sum += item['count']
print(sum)

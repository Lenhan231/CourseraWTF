import urllib2.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostnames = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the URL: ")
html = urllib.request.urlopen(url, context=ctx).read()
tags = BeautifulSoup(html, 'html.parser').find_all('a')
for tag in tags:
    print(tag.get('href'))
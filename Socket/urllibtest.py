from urllib.request import urlopen
from bs4 import BeautifulSoup

def opurl(url,check):
    if check != 6:
        response = urlopen(url)
        html_content = response.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        anchors = soup.find_all('a')
        for i in range(0,18):
            href = anchors[i].get('href')
        return opurl(href,check+1)
    else:
        response = urlopen(url)
        html_content = response.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        anchors = soup.find_all('li')
        for i in range(0,18):
            name = anchors[i].a.text
        print(name)
    
url = "https://py4e-data.dr-chuck.net/known_by_Sukhmani.html"
opurl(url,0)


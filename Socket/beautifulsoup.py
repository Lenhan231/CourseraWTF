'''from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
Elsie, Lacie and Tillie; and they lived at the bottom of a well.
...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())'''
from bs4 import BeautifulSoup
import requests

# HTML code
html_code = '<li style="margin-top: 16px;"><a href="http://py4e-data.dr-chuck.net/known_by_Aniqa.html">bAniqa</a></li>'

# Parse the HTML code
soup = BeautifulSoup(html_code, 'html.parser')

# Find the text within the <a> tag
aniqa_text = soup.a.text

# Print the result
print(aniqa_text)
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
Elsie, Lacie and Tillie; and they lived at the bottom of a well.
...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
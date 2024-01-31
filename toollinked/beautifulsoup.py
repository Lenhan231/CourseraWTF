import requests
from bs4 import BeautifulSoup

url = "https://py4e-data.dr-chuck.net/comments_1961948.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
comments_spans = soup.find_all('span', class_='comments')

total_comments = 0
for span in comments_spans:
    total_comments += int(span.text)

print(total_comments)

'''from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://py4e-data.dr-chuck.net/comments_1961948.html"

# Use urlopen to retrieve the HTML content
response = urlopen(url)
html_content = response.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all spans with the class 'comments'
comments_spans = soup.find_all('span', class_='comments')

total_comments = 0
for span in comments_spans:
    # Access the text content using .text and convert it to an integer
    total_comments += int(span.text)

print(total_comments)
'''
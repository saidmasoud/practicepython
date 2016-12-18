# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles
# on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

request = requests.get("http://www.nytimes.com/")

soup = BeautifulSoup(request.text, 'html.parser')

for article in soup.find_all("h2"):
    classs = str(article.get("class"))
    if 'story' in classs:
        print(article.find("a").string)

#print(soup.prettify())
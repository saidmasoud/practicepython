#Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on
# this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

#The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that
# you can read the full article without having to click any buttons.

#(Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries
# through the solution of the exercise posted here.)

#This will just print the full text of the article to the screen. It will not make it easy to read,
# so next exercise we will learn how to write this text to a .txt file.

# The article is now all on one page, so unfortunately I could not work on combining four-pages'
# worth of text into one :/ However, the below code still works.
# - Said

import requests
from bs4 import BeautifulSoup

request = requests.get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")

soup = BeautifulSoup(request.text, 'html.parser')

for paragraph in soup.find_all("p"):
    text = ""
    for content in paragraph:
        if isinstance(content,str):
            text+=content+"\n"
    if not content==None and paragraph.span==None:
        print(text)
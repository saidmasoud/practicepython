#Take the code from the How To Decode A Website exercise (exercise17.py), and instead of printing the results to
# a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

#Extras:

# Ask the user to specify the name of the output file that will be saved.

# ---------from exercise 17, placed into a function---------
import requests
from bs4 import BeautifulSoup

def get_articles(url):
    articles = ""
    request = requests.get(url)

    soup = BeautifulSoup(request.text, 'html.parser')

    for article in soup.find_all("h2"):
        classs = str(article.get("class"))
        # not all 'h2' tags have a sub-tags
        a_tag = article.find("a")
        if 'story' in classs and a_tag!=None:
            # not all the 'a' tags will have string values
            if a_tag.string!=None:
                articles+=(a_tag.string)+'\n'

    return articles
# --------------------end exercise 17---------------------
articles = get_articles("http://www.nytimes.com/")
file_name = input("Enter a filename: ")

file = open(file_name,'w')

file.write(articles)
file.close()
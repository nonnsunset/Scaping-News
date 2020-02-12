import requests
from pythainlp import word_tokenize
from bs4 import BeautifulSoup

url = "https://www.thaipost.net/main/detail/56506"
news = requests.get(url)
news.encoding = "utf-8"
soup = BeautifulSoup(news.text, 'html.parser')
titles = soup.find('h2')
date = soup.find('label')
print(titles.text + "\n")
print(date.text + "\n")
body = soup.find("div", class_ = "col-md-12 col-xs-12 contentDetail")

first = body.find('p')
while first != None:
    try:
        if first['style']:
            pass
    except:
        print(first.text)
    first = first.find_next_sibling('p')
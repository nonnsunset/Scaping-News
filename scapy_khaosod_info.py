import requests
from pythainlp import word_tokenize
from bs4 import BeautifulSoup

url = "https://www.khaosod.co.th/politics/news_3491337"
news = requests.get(url)
news.encoding = "utf-8"
soup = BeautifulSoup(news.text, 'html.parser')
titles = soup.find("h2")
date = soup.find("time", class_ = 'entry-date updated td-module-date')
print(titles.text)
print(date.text + "\n")
body = soup.find_all('p')
for content in body:
    print(content.text)


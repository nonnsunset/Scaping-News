import requests
from pythainlp import word_tokenize
from bs4 import BeautifulSoup

url = "https://www.thairath.co.th/news/politic/1752995"
news = requests.get(url)
news.encoding = "utf-8"
soup = BeautifulSoup(news.text, 'html.parser')
titles = soup.find("h1", {"class" : "css-s05tt0 e1ui9xgn0"})
date = soup.find("span", {"class" : "css-1o5avae e1ui9xgn2"})
print(titles.text)
print("\n")
content = soup.find_all("p")
for i in content:
    print(i.text)
print("\n")
print(date.text)
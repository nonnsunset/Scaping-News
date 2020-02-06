import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = "https://www.matichon.co.th/politics/news_1934814"
news = requests.get(url)
news.encoding = "utf-8"
soup = BeautifulSoup(news.text, 'html.parser')
titles = soup.find("h1", class_ = "entry-title")
date = soup.find("time", class_ = 'entry-date updated td-module-date')
print(titles.text + "\n")
print(date.text + "\n")
body = soup.find_all('p')
for content in body:
    print(content.text)

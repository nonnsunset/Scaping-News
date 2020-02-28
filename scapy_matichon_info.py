import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def get_info(url):
    news = requests.get(url)
    news.encoding = "utf-8"
    soup = BeautifulSoup(news.text, 'html.parser')
    titles = soup.find("h1", class_ = "entry-title")
    titles = titles.text
    date = soup.find("time", class_ = 'entry-date updated td-module-date')
    date = date.text
    data = soup.find_all('p')
    content = []
    for i in data:
        info = i.text
        content.append(info)
    body = ' '.join(content)
    return titles,date,body






    

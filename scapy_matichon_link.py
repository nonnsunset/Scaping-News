import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from scapy_matichon_info import get_info

driver = webdriver.PhantomJS(executable_path='/usr/local/lib/node_modules/phantomjs/lib/phantom/bin/phantomjs')
driver.get('https://www.matichon.co.th/politics')
def article_link(x):
    arr = []
    button = driver.find_element_by_xpath("//div[@class='page-nav td-pb-padding-side']//i[@class='td-icon-menu-right']")
    news = driver.page_source
    soup = BeautifulSoup(news, 'html.parser')
    get_link = soup.find_all("div", class_ = "td_module_10 td_module_wrap td-animation-stack")
    for i in range(x):
        button.click()
    
    for i in get_link:
        i = i.find("div",class_ = "td-module-thumb").find('a')
        news_link = i['href']
        arr.append(news_link)
    return arr

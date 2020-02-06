import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path='/usr/local/lib/node_modules/phantomjs/lib/phantom/bin/phantomjs')
driver.get('https://www.thaipost.net/main/category/1')

for x in range(4):
    button = driver.find_element_by_xpath("//ul[@class='pagination']//li[@class='next']//a//i[@class='fa fa-chevron-right']")
    news = driver.page_source
    soup = BeautifulSoup(news, 'html.parser')
    get_link = soup.find_all("a", class_ = "post-title")
    for i in get_link:
        print(i['href'])
    button.click()
    #time.sleep(1)
    print("click next")
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path='/usr/local/lib/node_modules/phantomjs/lib/phantom/bin/phantomjs')
driver.get('https://www.matichon.co.th/politics')


for x in range(4):
    button = driver.find_element_by_xpath("//div[@class='page-nav td-pb-padding-side']//i[@class='td-icon-menu-right']")
    news = driver.page_source
    soup = BeautifulSoup(news, 'html.parser')
    get_link = soup.find_all("div", class_ = "td_module_10 td_module_wrap td-animation-stack")
    for i in get_link:
        i = i.find("div",class_ = "td-module-thumb").find('a')
        print(i['href'])
    button.click()
    #time.sleep(1)
    print("click next")
import requests
from pythainlp import word_tokenize
from bs4 import BeautifulSoup
import json
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='/usr/local/lib/node_modules/phantomjs/lib/phantom/bin/phantomjs')
driver.get('https://www.thairath.co.th/news/politic')
button = driver.find_element_by_xpath("//div[@class='css-fyizue e1hphrsb1']")
for x in range(5):
    button.click()
    print(len(driver.page_source))
news = driver.page_source


# url = "https://www.thairath.co.th/news/politic"
# news = requests.get(url)
# news.encoding = "utf-8"
soup = BeautifulSoup(news, 'lxml')
get_link = soup.find_all("div", {"class" : "css-1ugzggj e9fvmtc0"})
for i in get_link:
    print(i)
# for highlight in get_link:
#     tags = soup.select("[type = 'application/json']")[0]
#     highlight = json.loads(tags.text)["props"]["initialState"]["common"]["data"]["items"]["highlight"]
#     for i in highlight:
#         print(i['canonical'])
# for other in get_link:
#     tags = soup.select("[type = 'application/json']")[0]
#     other = json.loads(tags.text)["props"]["initialState"]["common"]["data"]["items"["scoop"]
#     for i in other:
#         print(i['canonical'])

# tags = soup.select("[type = 'application/json']")
# popular = json.loads(tags[0].text)["props"]["initialState"]["news"]["data"]["items"]["lastestNews"]
# for i in popular:
#     print(i['canonical'])

# popular = json.loads(tags[0].text)["props"]["initialState"]["news"]["data"]["items"]["breakingNews"]
# for i in popular:
#     print(i['canonical'])

# for breakingNews in get_link:
#     tags = soup.select("[type = 'application/json']")[0]
#     breakingNews  = json.loads(tags.text)["props"]["initialState"]["common"]["data"]["items"]["breakingNews"]
#     for i in breakingNews :
#         print(i['canonical'])
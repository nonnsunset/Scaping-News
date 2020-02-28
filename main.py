from scapy_matichon_link import article_link as link_matichon
from scapy_matichon_info import get_info
from connect_firebase import update_news
import re

def main():
    list_link = link_matichon(0)
    for i in list_link:
        titles,date,body = get_info(i)
        news = {"body" :body, "title" :titles, "date" :date, "url" :i}
        a = re.sub(r'[^\w]','',i[12:])

        update_news("matichon/"+a, news)
main()
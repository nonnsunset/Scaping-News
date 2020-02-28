import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
cred = credentials.Certificate('/Users/natchanonwongsawaddiwattana/Documents/Doc_Non/scapy-news-firebase-adminsdk-s90jw-21835f16ca.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://scapy-news.firebaseio.com/'
})


def update_news(agent,news):
    ref = db.reference('/news/'+agent)
    print(ref.update(news))
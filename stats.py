import re
import requests
import pymysql
from bs4 import BeautifulSoup


def getPlayerList(url):
    request = requests.get(url)
    data = request.text[17,-1]
    str = []
    for item in data['data']['players']:
        if item[3]==1:
            str.append('http://stats.nba.com/player/'+item[0])



    return soup.


def searchDetails(url):
    pass;


def saveToMysql(cursor,info):
    pass;


def main():
    listUrl = "http://stats.nba.com/js/data/ptsd/stats_ptsd.js"
    players = getPlayerList(listUrl)
    db = pymysql.connect('167.88.162.185','user','12345qwert','nba')
    print('database has been connected')
    cur = db.cursor()
    for player in players:
        print(player)
        detail = searchDetails(player)
        saveToMysql(cur, detail)
    cur.close()
    db.close()

main()
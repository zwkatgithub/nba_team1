import json
import requests
import pymysql
from bs4 import BeautifulSoup


def getPlayerList(url):
    request = requests.get(url)
    data = request.text[17:-1]
    players = []
    for item in json.loads(data)['data']['players']:
        if item[2]==1:
            players.append('http://stats.nba.com/player/'+str(item[0]))
    return players


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
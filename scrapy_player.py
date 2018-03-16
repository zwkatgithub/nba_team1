from uscarp import *
import json
from bs4 import BeautifulSoup


def getPlayerList(url):
    data = getHtml(url)[17:-1]
    players = []
    for item in json.loads(data)['data']['players']:
        if item[2]==1:
            players.append('http://stats.nba.com/player/'+str(item[0]))
    return players


def searchDetails(url):
    soup = BeautifulSoup(getDHtml(url),'lxml')
    spans = soup.select('span.player-stats__stat-value')
    infos = [span.get_text() for span in spans]
    print(infos)
    # summary = {'height':infos[4],'weight':infos[5],
    pass;


def saveToMysql(cursor,info):

    pass;


def main():
    listUrl = "http://stats.nba.com/js/data/ptsd/stats_ptsd.js"
    players = getPlayerList(listUrl)
    sql = sMysql('sonp_nba')
    for player in players:
        detail = searchDetails(player)
        saveToMysql(sql.cur, detail)
main()
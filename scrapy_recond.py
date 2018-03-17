from uscarp import *

def getPlayerIds(db):
    sql = 'select id from player_info;'
    db.execute(sql)
    data = []
    for item in db.content():
        data.append(item[0])
    return data


def getRecords(db,id):
    url = 'http://stats.nba.com/stats/playerdashboardbyyearoveryear?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00' \
          '&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID='
    url +=str(id)
    url +='&PlusMinus=N&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&Split=yoy&VsConference=&VsDivision='
    js = getHtml(url,timeout=30)
    if not js:
        return None
    info = json.loads(js)['resultSets'][1]
    header = info['headers']
    header = ['player_id']+header[1:3]+header[5:34]
    for rowset in info['rowSet']:
        rowset = [id]+rowset[1:3]+rowset[5:34]
        saveToMysqlByList(db,'record',header,rowset)

def main():
    db = sMysql('sonp')
    ids = getPlayerIds(db)
    for id in ids:
        getRecords(db,id)
        db.commit()


if __name__ == '__main__':
    main()
from uscarp import *


def getPlayerList(url):
    data = getHtml(url)[17:-1]
    players = []
    for item in json.loads(data)['data']['players']:
        if item[2]==1:
            players.append('http://stats.nba.com/player/'+str(item[0]))
    return players


def searchDetails(url):
    pattern = re.compile(r'window.nbaStatsPlayerInfo = (.+?);')
    info = pattern.search(getHtml(url)).group(1)
    info = json.loads(info)
    summary = {'id':info['PERSON_ID'],'height':info['HEIGHT'],'weight':info['WEIGHT'],'name':info['FIRST_NAME']+' '+info['LAST_NAME'],
               'team_id':info['TEAM_ID'],'pos':info['POSITION_INITIALS'],'birthdate':info['BIRTHDATE'],'country':info['COUNTRY'],
               'school':info['SCHOOL']}
    return summary


def saveToMysql(cursor,info):
    first = 'INSERT INTO player_info('
    second = ') VALUES('
    for key in info:
        if key !='id':
            first += ','
            second += ','
        first += key
        if isinstance(info[key],str):
            second += '\''+str(info[key])+'\''
        else :
            if info[key] == None:
                info[key] = 'null'
            second += str(info[key])
    sql = first+second+');'
    print(sql)
    cursor.execute(sql,True)


def main():
    listUrl = "http://stats.nba.com/js/data/ptsd/stats_ptsd.js"
    players = getPlayerList(listUrl)
    sql = sMysql('sonp_nba')
    for player in players:
        detail = searchDetails(player)
        saveToMysql(sql.cur, detail)
main()
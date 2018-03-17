from uscarp import *


def getPlayerList(url):
    data = getHtml(url)[17:-1]
    players = []
    for item in json.loads(data)['data']['players']:
        if item[2]==1:
          players.append('http://stats.nba.com/player/'+str(item[0]))
    return players


def getDetails(db, url):
    pattern = re.compile(r'window.nbaStatsPlayerInfo = (.+?);')
    html = getHtml(url)
    if html == None:
        return None
    info = pattern.search(html).group(1)
    info = json.loads(info)
    summary = {'id':info['PERSON_ID'],'height':info['HEIGHT'],'weight':info['WEIGHT'],'name':info['FIRST_NAME']+' '+info['LAST_NAME'],
               'team_id':info['TEAM_ID'],'pos':info['POSITION_INITIALS'],'birthdate':info['BIRTHDATE'],'country':info['COUNTRY'],
               'school':info['SCHOOL']}
    saveToMysql(db,'player_info',summary)


def main():
    listUrl = "http://stats.nba.com/js/data/ptsd/stats_ptsd.js"
    players = getPlayerList(listUrl)
    db = sMysql('sonp')
    for player in players:
        getDetails(db, player)
main()
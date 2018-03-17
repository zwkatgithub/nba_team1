from uscarp import *

def getTeamList(url):
    html = dHtml(30).get(url)
    soup  = BeautifulSoup(html,"lxml")
    hrefs = soup.select("a.stats-team-list__link")
    return ["http://stats.nba.com/stats/teamdetails?teamID="+href["href"][6:-1] for href in hrefs]

def getDetail(db, url):
    print(url)
    detail = json.loads(getHtml(url))["resultSets"][0]["rowSet"][0]
    infos = {"id":detail[0],"name":detail[2],"abbr":detail[1],"found_year":detail[3],"city":detail[4],"arena":detail[5],
            "manager":detail[8],"head_coach":detail[9],"owner":detail[7]}
    saveToMysql(db,"team_info",infos)


def main():
    url = "http://stats.nba.com/teams/"
    teams = getTeamList(url)
    db = sMysql("sonp")
    for team in teams:
        getDetail(db, team)

main()

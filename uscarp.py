import requests
import pymysql
from selenium import webdriver



def getHtml(url, code='utf-8'):
    res = requests.get(url,timeout=20)
    res.encoding = code
    return res.text


def getDHtml(url):
    option = webdriver.ChromeOptions()
    option.set_headless()
    driver = webdriver.Chrome(options=option)
    driver.set_page_load_timeout(20)
    try:
        driver.get(url)
    except:
        pass
    try:
        res = driver.page_source
    except:
        res = None
    driver.close()
    return res


class sMysql:
    uhost = '167.88.162.185'
    uuser = 'user'
    upswd = '12345qwert'

    def __init__(self,schema,user=uuser,pswd=upswd,host=uhost):
        self.db = pymysql.connect(host,user,pswd,schema)
        self.cur = self.db.cursor()
        print("connected to %s@%s use %s!"%(user,host,schema))

    def excute(self,sql,commit=False):
        self.cur.execute(sql)
        if commit:
            try:
                self.db.commit()
                print("successfully commit!")
            except:
                print("! cannot commit")
                self.db.rollback()

    def content(self,all=True):
        try :
            if all:
                return self.cur.fetchall()
            else :
                return self.cur.fetchone()
        except:
            print("can't get content")

    def __del__(self):
        self.cur.close()
        self.db.close()
        print("!close connection to %s@%s"%(self.db.user,self.db.host))
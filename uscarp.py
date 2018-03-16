import json
import re
import requests
import pymysql
from selenium import webdriver
from bs4 import BeautifulSoup



def getHtml(url, code='utf-8',timeout=30):
    res = requests.get(url, timeout=timeout)
    res.encoding = code
    return res.text


class dHtml:
    def __init__(self, timeout=20):
        option = webdriver.ChromeOptions()
        option.set_headless()
        self.driver = webdriver.Chrome(options=option)
        self.driver.set_page_load_timeout(timeout)

    def get(self,url):
        try:
            self.driver.get(url)
        except:
            pass
        try:
            return self.driver.page_source
        except:
            return None

    def __del__(self):
        self.driver.close()



class sMysql:
    uhost = '167.88.162.185'
    uuser = 'user'
    upswd = '12345qwert'

    def __init__(self,schema,user=uuser,pswd=upswd,host=uhost):
        self.db = pymysql.connect(host,user,pswd,schema)
        self.cur = self.db.cursor()
        print("connected to %s@%s use %s!"%(user,host,schema))

    def excute(self,sql):
        self.cur.execute(sql)

    def commit(self):
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
        # self.commit()
        self.cur.close()
        self.db.close()
        print("!close connection to %s@%s"%(self.db.user,self.db.host))
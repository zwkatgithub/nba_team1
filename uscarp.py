import json
import re
import requests
import pymysql
from selenium import webdriver
from bs4 import BeautifulSoup

class sLog:

    def __init__(self):
        self.log = []
        print("start to log errors")

    def add(self,e):
        self.log.append(e)

    def __del__(self):
        if self.log:
            print("some errors occurred during the processing:")
            for e in self.log:
                print(e)


log = sLog()


def getHtml(url, code='utf-8', timeout=15):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6"}
    try:
        res = requests.get(url, timeout=timeout, headers=headers)
        res.encoding = code
        return res.text
    except Exception as e:
        log.add(str(e)+url)
        return None


def saveToMysql(db, table, info):   #By Dict
    first = 'INSERT INTO %s('%table
    second = ') VALUES('
    for key in info:
        first += key+','
        if isinstance(info[key],str):
            second += '\"'+str(info[key])+'\",'
        else :
            if info[key] == None:
                info[key] = 'null'
            second += str(info[key])+','
    sql = first[:-1]+second[:-1]+');'
    # print(sql)
    db.execute(sql)


def saveToMysqlByList(db, table, headers, values):
    sql = 'INSERT INTO %s('%table
    for header in headers:
        sql +=header+','
    sql =sql[:-1]+') VALUES('
    for value in values:
        if isinstance(value, str):
            sql += '\"'+str(value)+'\",'
        else :
            if value == None:
                value = 'null'
            sql += str(value)+','
    sql = sql[:-1]+');'
    # print(sql)
    db.execute(sql)


class dHtml:
    def __init__(self, timeout=20):
        option = webdriver.ChromeOptions()
        # option.set_headless()
        self.driver = webdriver.Chrome(options=option)
        self.driver.set_page_load_timeout(timeout)

    def get(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            log.add(e)
        try:
            return self.driver.page_source
        except Exception as e:
            log.add(e)
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

    def execute(self, sql):
        try:
            self.cur.execute(sql)
        except Exception as e:
            log.add(e)

    def commit(self):
        try:
            self.db.commit()
            print("successfully commit!")
        except Exception as e:
            log.add(e)
            print("! cannot commit")
            self.db.rollback()

    def content(self, all=True):
        try :
            if all:
                return self.cur.fetchall()
            else :
                return self.cur.fetchone()
        except Exception as e:
            log.add(e)
            print("can't get content")

    def __del__(self):
        self.commit()
        self.cur.close()
        self.db.close()
        print("!close connection to %s @ %s"%(self.db.user, self.db.host))
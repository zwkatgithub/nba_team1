import pymysql
db = pymysql.connect('192.168.0.251', 'team1', '12345qwert', 'zwk')
cur = db.cursor()
data = cur.execute('select * from test;')
print(data.fetchall())
import pymysql

id = '201311611405'
user = '陈志远'
age = '18'

db = pymysql.connect(host='127.0.0.1',user='root',password='20110120YQ',port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name, age) values(%s,%s,%s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except:
    db.rollback()
db.close()

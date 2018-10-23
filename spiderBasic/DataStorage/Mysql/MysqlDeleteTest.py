import pymysql

db = pymysql.connect(host='127.0.0.1',user='root',password='20110120YQ',port=3306, db='spiders')
cursor = db.cursor()
table = 'students'
condition = 'age< 20'

sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()

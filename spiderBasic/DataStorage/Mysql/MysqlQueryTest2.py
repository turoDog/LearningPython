import pymysql

db = pymysql.connect(host='127.0.0.1',user='root',password='20110120YQ',port=3306, db='spiders')
cursor = db.cursor()
table = 'students'
sql = 'SELECT * FROM {table} WHERE age >= 20'.format(table=table)
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row', row)
        row = cursor.fetchone()
except:
    print('Error')

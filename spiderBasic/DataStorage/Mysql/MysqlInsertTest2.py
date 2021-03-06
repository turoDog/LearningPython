import pymysql

db = pymysql.connect(host='127.0.0.1',user='root',password='20110120YQ',port=3306, db='spiders')
cursor = db.cursor()
data = {
    'id' : '201311611406',
    'name' : '陈志远',
    'age' : 20
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()

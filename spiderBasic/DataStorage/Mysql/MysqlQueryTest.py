import pymysql

db = pymysql.connect(host='127.0.0.1',user='root',password='20110120YQ',port=3306, db='spiders')
cursor = db.cursor()

table = 'students'
sql = 'SELECT * FROM {table} WHERE age >= 20'.format(table=table)

try:
    cursor.execute(sql)
    print('Count:',cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall()
    print('Result:', results)
    print('Results Type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')

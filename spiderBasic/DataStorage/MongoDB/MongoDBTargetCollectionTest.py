import pymongo

# 指定数据库
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.test
# 指定集合
collection = db.students

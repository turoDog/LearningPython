import pymongo

# 指定数据库
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.test
# 指定集合
collection = db.students

# 根据字段排序
results = collection.find().sort('name', pymongo.ASCENDING)
print([result['name'] for result in results])

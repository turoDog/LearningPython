import pymongo
from bson.objectid import ObjectId

# 指定数据库
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.test
# 指定集合
collection = db.students

# 对查询结果进行偏移
results = collection.find().sort('name',pymongo.ASCENDING).skip(2)
print([result['name'] for result in results])

# 对查询结果进行偏移并限制
results1 = collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results1])

# 对查询结果进行偏移,数据量特别大时应该是用如下方法防止溢出
results2 = collection.find({'_id': {'$gt': ObjectId('5bd47e91a12e0f2c28ff901c')}})
print([result['name'] for result in results2])

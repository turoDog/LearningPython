import pymongo
from bson.objectid import ObjectId

# 指定数据库
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.test
# 指定集合
collection = db.students

# 查询一个（根据字段查询）
result = collection.find_one({'name' : 'Google'})
print(type(result))
print(result)

# 查询一个（根据id查询）
result1 = collection.find_one({'_id': ObjectId('5bd47e91a12e0f2c28ff901b')})
print(result1)

# 查询多个（根据字段查询, age = 24）
results = collection.find({'age':24})
print(results)
for item in results:
    print(item)

# 查询多个（根据字段查询, age > 24）
results1 = collection.find({'age':{'$gt': 20}})
print(results1)
for item in results1:
    print(item)

# 查询多个（根据正则查询, 名字以 G 开头）
results2 = collection.find({'name':'^G.*'})
print(results2)
for item in results2:
    print(item)

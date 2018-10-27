import pymongo

# 指定数据库
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.test
# 指定集合
collection = db.students

# 删除
result = collection.remove({'name':'Tesla'})
print(result)

# delete_one
result1 = collection.delete_one({'name': 'Alibaba'})
print(result1)
print(result1.deleted_count)

result2 = collection.delete_many({'age': {'$gt': 25}})
print(result2.deleted_count)

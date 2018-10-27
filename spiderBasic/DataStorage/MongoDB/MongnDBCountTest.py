import pymongo

# 指定数据库
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.test
# 指定集合
collection = db.students

# 统计所有数据条数
count = collection.find().count()
print(count)

# 统计某个符合条件的数据条数
count1 = collection.find({'age': 24}).count()
print(count1)

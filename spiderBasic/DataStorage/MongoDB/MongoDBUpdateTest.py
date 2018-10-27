import pymongo

# 指定数据库
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.test
# 指定集合
collection = db.students

# 进行更新
condition = {'name': 'Google'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update(condition,student)
print(result)

# 进行更新（用 $set）
condition = {'name': 'Apple'}
student1 = collection.find_one(condition)
student1['age'] = 30
result1 = collection.update(condition,{'$set' : student1})
print(result1)

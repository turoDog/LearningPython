import pymongo

# 指定数据库
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.test
# 指定集合
collection = db.students
# 即将插入的数据
student1 = {
    'id' : '20180104',
    'name' : '陈志远',
    'age' : '24',
    'gender' : 'male'
}
student2 = {
    'id' : '20180105',
    'name' : '陈志远',
    'age' : '24',
    'gender' : 'male'
}
result = collection.insert_many([student1,student2])
print(result)
print(result.inserted_ids)

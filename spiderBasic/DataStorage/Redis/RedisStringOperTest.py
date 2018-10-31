from redis import StrictRedis, ConnectionPool

# Reids 使用 ConnectionPool 来连接
pool = ConnectionPool(host='localhost', port=6379, db=0)
redis = StrictRedis(connection_pool=pool)

# 给数据库中的 key 赋值
# print(redis.set('name1','Bob'))

# 通过 key 获取 value
# print(redis.get('name1'))

# 给旧 key 设置新 value 返回旧 value
# print(redis.getset('name1','Mike'))

# 返回多个 key 对应的 value
# print(redis.mget(['name','name1']))

# 如果不存在该 key-value 对，则更新 value,否则不变
print(redis.setnx('newname','James'))

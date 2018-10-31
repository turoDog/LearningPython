from redis import StrictRedis, ConnectionPool

# Reids 使用 ConnectionPool 来连接
pool = ConnectionPool(host='localhost', port=6379, db=0)
redis = StrictRedis(connection_pool=pool)

# 在键为 list 的列表末尾添加值为 value 的元素(可多个)
# print(redis.rpush('list',1,2,3))

# 在键为 list 的列表头添加值为 value 的元素（可多个）
# print(redis.lpush('list',0))

# 返回 key 为 list 的列表的长度
print(redis.llen('list'))

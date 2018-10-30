from redis import StrictRedis, ConnectionPool

# Reids 使用 ConnectionPool 来连接
pool = ConnectionPool(host='localhost', port=6379, db=0)
redis = StrictRedis(connection_pool=pool)

# 是否存在key
print(redis.exists('name'))

# 删除key
print(redis.delete('age'))

# key的类型
print(redis.type('name'))

# 符合规则的key
print(redis.keys('n*'))

# 获取随机key
print(redis.randomKey())

# 重命名key
print(redis.rename('nick', 'nickname'))

# 获取key的数目
print(redis.dbsize())

# 设置 key 的过期时间
print(redis.expire('name', 2))

# 获取key的过期时间
print(redis.ttl('name'))

# 将 key 移动到其他数据库
print(redis.move('nickname',2))

# 删除当前选择数据库中的所有 key
print(redis.flushdb())

# 删除所有数据库中的所有 key
print(redis.flushall())

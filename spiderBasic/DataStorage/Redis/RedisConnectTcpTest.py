from redis import StrictRedis, ConnectionPool

# 创建 Redis TCP 连接
url = 'redis://:@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)

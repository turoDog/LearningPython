from redis import StrictRedis, ConnectionPool

# Reids 使用 ConnectiionPool 来连接
pool = ConnectionPool(host='localhost', port=6379, db=0)
redis = StrictRedis(connection_pool=pool)

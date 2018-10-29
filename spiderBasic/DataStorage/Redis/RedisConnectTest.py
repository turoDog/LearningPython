from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0)
redis.set('name', '陈志远')
print(redis.get('name'))

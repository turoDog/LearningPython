from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0)
redis.set('nick', 'nasus')
print(redis.get('nick'))

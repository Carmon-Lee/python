from learning import redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)

r = redis.Redis(connection_pool=pool)
r2 = redis.Redis(connection_pool=pool)
r.set('apple', 'a')
print(r.get('apple'))
r2.set('banana', 'b')
print(r.get('banana'))

print(r.client_list())
print(r2.client_list())  # 可以看出两个连接的id是一致的，说明是一个客户端连接


def test():
    print('test')
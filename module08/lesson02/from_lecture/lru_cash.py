import redis
from redis_lru import RedisLRU

client  = redis.Redis(host='localhost',
                 port=6379,
                 db=0)
cache = RedisLRU(client)


@cache
def f(x):
    print(f"Function call f({x})")
    return x


if __name__ == '__main__':
    print(f"First f(3): {f(3)}")
    print(f"Second f(3): {f(3)}")
    
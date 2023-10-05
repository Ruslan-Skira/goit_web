import redis
try:

    r = redis.Redis(host='localhost',
                 port=6379,
                 db=0)
    r.ping()  # This will attempt to ping the server, and if successful, you're connected.
    print("Connected to Redis")

    r.set('foo', 'bar')
    value = r.get('foo')
    print(value)    # bar
except redis.ConnectionError:
    print("Could not connect to Redis")

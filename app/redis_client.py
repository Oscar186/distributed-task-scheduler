import redis

try:
    r = redis.Redis(host='localhost', port=6379, db=0)
    print("Redis ping:", r.ping())
except Exception as e:
    print("Redis connection failed:", e)

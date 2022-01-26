import time
MAX_CACHE_SIZE = 3

def put(cache, key, value):
    # ak je v cache rovny max tak popne prvy ak nie prida do cache dalcie data
    if len (cache) == MAX_CACHE_SIZE:
        cache.pop(next(iter(cache)))
    cache[key]=value
    
def get(cache, key):
    return cache.get(key)
    
print(time.time())

CACHE = {}

put(CACHE, 'a', 10)
print(get(CACHE, 'a'))
put(CACHE, 'b', 20)
put(CACHE, 'c', 30)
put(CACHE, 'd', 40)
print(get(CACHE, 'c'))
print(get(CACHE, 'a'))

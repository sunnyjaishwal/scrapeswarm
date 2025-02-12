import redis
import json

class CacheService:
    def __init__(self, host='localhost', port=8084, db=0):
        self.client = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    def get_cache(self, source, destination, date, siteid):
        key = f"{source}:{destination}:{date}:{siteid}"
        cached_data = self.client.get(key)
        if cached_data:
            return json.loads(cached_data)
        return False
    
    def set_cache(self, key, value, expiration: int =None):
        
        self.client.set(key, json.dumps(value), ex=expiration)
        return True

# Example usage:
# cache_service = CacheService()
# data = cache_service.get_cache('source1', 'destination1', '2023-10-01', 'siteid1')
# if data:
#     print("Cache hit:", data)
# else:
#     print("Cache miss")
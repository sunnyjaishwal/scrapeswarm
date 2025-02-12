from typing import Union

from fastapi import FastAPI # type: ignore

from models.InputData import InputData
from services.cache_service import CacheService

app = FastAPI()


@app.post("/send_request")
async def send_request(data: InputData):
    # verify the data

    cache = CacheService()
    # checking the cache for the available response
    response = cache.get_cache(data.sourceIATA, data.destinationIATA, data.departureDate, data.siteId)
    if response:
        return {"details":response,
                "message": "Response retrieved from cache"}
    else:
        print("cache miss")
        # if not available, send request to message broker
        # message broker will send the request to the spider
        # spider will send the response to the message broker
        # message broker will send the response to the cache
        
        
        key = f"{data.sourceIATA}:{data.destinationIATA}:{data.departureDate}:{data.siteId}"
        value = {"sourceIATA": data.sourceIATA, "destinationIATA": data.destinationIATA, "departureDate": data.departureDate, "siteId": data.siteId}
        cache.set_cache(key, value, expiration=60)

        # cache will send the response to the client

        return {"details":"Response added to cache"}

   
   
    
    
    
    
    return data
from urllib.request import Request, urlopen

from google.transit import gtfs_realtime_pb2


feed = gtfs_realtime_pb2.FeedMessage()
req = Request('https://gtfsr.transportforireland.ie/v1')
req.add_header('x-api-key', 'xxxxxx')
response = urlopen(req)
feed.ParseFromString(response.read())
#print (feed.entity[0])
for entity in feed.entity:
    if entity.HasField('trip_update'):
        x=feed.entity
        print(x)  
        #print(feed.entity.values)

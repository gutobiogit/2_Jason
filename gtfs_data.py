from google.transit import gtfs_realtime_pb2
from urllib2.request import request,urlopen

feed = gtfs_realtime_pb2.FeedMessage()
response = urlopen('https://gtfsr.transportforireland.ie/v1/?format=json?key=AIzaSyCu4ueJS6dPolvynHjJ9QM_iyALJL10Mzc')
feed.ParseFromString(response.read())
for entity in feed.entity:
  if entity.HasField('trip_update'):
    print (entity.trip_update)




import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
# Request headers
'Cache-Control': 'no-cache',
'x-api-key': '05a8cca127b04076832bd54d93d46ff2',
}

params = urllib.parse.urlencode({
})

try:
conn.request("GET", "?%s" % params, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))




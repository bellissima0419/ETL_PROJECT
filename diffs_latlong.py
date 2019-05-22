from math import sin, cos, sqrt, atan2, radians
import math
import json
fname = 'us-zip-code-latitude-and-longitude.json'
loadedLatLongData = json.load(open(fname))


def distanceV(lat1, lon1,lat2, lon2):
    #lat1, lon1 = origin
    #lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

def computeNearestZip(latitude, longitude):
    smallestDistance = 1000000
    smallestZip = None
    for data in loadedLatLongData:
        if ("fields" in data):
            distancedata = data["fields"]
            if("latitude" in distancedata and "longitude" in distancedata and "zip" in distancedata):
                zipcode = distancedata["zip"]
                lat1 = distancedata["latitude"]
                long1 = distancedata["longitude"]
                distance = distanceV(latitude,longitude, lat1,long1)

                if(distance <smallestDistance):
                    smallestZip = zipcode
                    smallestDistance = distance


    # return smallestDistance, smallestZip
    return smallestZip

if __name__ == '__main__':
    #lat long of 30339
    smallestDistance, smallestZip = computeNearestZip(33.8677, -84.4645)
    print(smallestZip)
    print(smallestDistance)

    #lat long of 27510
    smallestDistance, smallestZip = computeNearestZip(35.9108, -79.0815)
    print(smallestZip)
    print(smallestDistance)

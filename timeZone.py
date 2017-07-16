try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json
import datetime

def geolocation():
    send_url = "http://freegeoip.net/json"
    response = urlopen(send_url)
    data = json.loads(response.read())
    #lat = data['latitude']
    #lon = data['longitude']
    country = data['country_code']
    zone = data['time_zone']
    zoneName =zone.replace("/","\/")
    op = [country,zoneName]
    return op

request = geolocation()
url = ("http://api.timezonedb.com/v2/list-time-zone?key=AV7PO92VO9NU&format=json&country="+str(request[0])+"&zone=*"+str(request[1])+"*")
def get_jsonparsed_data(url):
    if url:
        response = urlopen(url)
        data = json.loads(response.read())
        return data

def get_timeStamp(data):
    timeStm = data['zones'][0]['timestamp']
    return timeStm

def ConvertToDateTime(timestamp):
    # Egypt TimeZone (-(60*60)*2))
    return datetime.datetime.fromtimestamp(int(timestamp)-(60*60)*2).strftime('%Y-%m-%d %I:%M:%S')

items = get_jsonparsed_data(url)
timeStamp = get_timeStamp(items)
timeZone = ConvertToDateTime(timeStamp)
print(timeZone)
print("Country: "+request[0]+"\n" + "Zone: "+ request[1] +"\n")
from data import IPsInfo, IPsByCountry
from ipConversion import ipToInt
import json


class GeoInfo:
    def __init__(self, countryID, countryName):
        self.countryID = countryID
        self.countryName = countryName
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

class CountryAllIP:
    def __init__(self, countryID):
        self.countryID = countryID
        self.countryIPs = IPsByCountry[countryID]
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

def ipToGeoInfo(ipStr):
    intIp = ipToInt(ipStr)
    print(intIp)
    begin = 0
    end = len(IPsInfo) - 1
    geoInfo = None
    while begin <= end:
        mid = begin + (end - begin) // 2
        _from, to = IPsInfo[mid][0][0], IPsInfo[mid][0][1]
        if _from <= intIp <= to:
            ID, name = IPsInfo[mid][1][0], IPsInfo[mid][1][1]
            geoInfo = GeoInfo(ID, name)
            break
        if intIp < _from:
            end = mid - 1
        if intIp > to:
            begin = mid+1
    return geoInfo


def countryIPs(countryID):
    if countryID not in IPsByCountry.keys():
        return None
    return CountryAllIP(countryID)


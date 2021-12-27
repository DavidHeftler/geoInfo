from flask import Flask
from IpGeoInfo import ipToGeoInfo, countryIPs
import data
import json

app = Flask(__name__)

class Error:
    def __init__(self, errorName):
        self.errorName = errorName

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


@app.route('/')
def Nothing():
    return Error('nothing to see here, try adding "/GeoInfo"').toJSON()


@app.route('/GeoInfo')
def AddEndPoint():
    return Error('for Geo information about an IP address, add "/IpToGeoInfo/(the ip address)". '
                 'for all IP addresses of a country, add' 
                 '"/CountryIPs/(the country initials)').toJSON()


@app.route('/GeoInfo/IpToGeoInfo/<string:ip>')
def getIpData(ip):
    info = ipToGeoInfo(ip)
    if info is None:
        return Error("no information about this IP").toJSON()
    if info is False:
        return Error("IP not legal!").toJSON()
    return info.toJSON()


@app.route('/GeoInfo/CountryIPs/<string:countryID>')
def getCountryIPs(countryID):
    countryAllIPs = countryIPs(countryID)
    if countryAllIPs is None:
        return Error("Country not found!").toJSON()
    return countryAllIPs.toJSON()


if __name__ == '__main__':
    data.loadIpData()
    app.run()

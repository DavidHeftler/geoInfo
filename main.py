from flask import Flask
from IpGeoInfo import ipToGeoInfo, countryIPs
import data

app = Flask(__name__)


@app.route('/GeoInfo')
def AddEndPoint():
    return 'for Geo information about an IP address, add \"/IpToGeoInfo/(the ip address)\"'


@app.route('/GeoInfo/IpToGeoInfo/<string:ip>')
def getIpData(ip):
    info = ipToGeoInfo(ip)
    if info is None:
        return "IP not found!"
    return info.toJSON()


@app.route('/GeoInfo/CountryIPs/<string:countryID>')
def getCountryIPs(countryID):
    countryAllIPs = countryIPs(countryID)
    if countryAllIPs is None:
        return "Country not found!"
    return countryAllIPs.toJSON()

if __name__ == '__main__':
    data.loadIpData()
    app.run()

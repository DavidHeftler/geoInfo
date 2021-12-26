from flask import Flask
import IpGeoInfo
import data

app = Flask(__name__)


@app.route('/GeoInfo')
def AddEndPoint():
    return 'for Geo information about an IP address, add \"/IpToGeoInfo/(the ip address)\"'


@app.route('/GeoInfo/IpToGeoInfo/<string:ip>')
def getIpData(ip):
    info = IpGeoInfo.ipToGeoInfo(ip)
    if info is None:
        return "IP not found!"
    return info.toJSON()


if __name__ == '__main__':
    data.loadIpData()
    app.run()

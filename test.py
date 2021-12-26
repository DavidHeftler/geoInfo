import requests


url = requests.get("http://127.0.0.1:5000/GeoInfo/IpToGeoInfo/10.10.10.10")
text = url.text
print(text)
print(type(text))



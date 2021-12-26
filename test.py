import requests

url = requests.get("http://127.0.0.1:5000/")
print(url.text)

url = requests.get("http://127.0.0.1:5000/GeoInfo")
print(url.text)

url = requests.get("http://127.0.0.1:5000/GeoInfo/IpToGeoInfo/10.10.10.10")
text = url.text
print(text)


url = requests.get("http://127.0.0.1:5000/GeoInfo/CountryIPs/IL")
text = url.text
print(text)





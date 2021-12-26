import requests

url = "http://127.0.0.1:5000/"

response = requests.get(url)
print(response.text)

response = requests.get(url +"/GeoInfo")
print(response.text)

response = requests.get(url + "/GeoInfo/IpToGeoInfo/10.10.10.10")
print(response.text)

response = requests.get(url + "/GeoInfo/IpToGeoInfo/293.75.41.50")
print(response.text)

response = requests.get(url + "/GeoInfo/CountryIPs/DE")
print(response.text)





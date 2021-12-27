# proofpoint
OverView:
This program runs a web application for receiving geographic information about countries and their IP addresses.
The website exposes two endPoints:
1. IpToGeoInfo:
   A service for receiving geographic information about a given IP address
2. CountryIPs:
   A service for receiving all IP addresses of a given country ID
All information is based on the IP2LOCATION-LITE-DB1.CSV file, which can be found at https://download.ip2location.com/lite/.

Instruction- Deploy Server: 
1. Clone repository.
 from cmd:
2. cd [the project directory]
3. python3.10 -m pip install -r requirements.txt
4. python3.10 main.py 

the base url for the program is "http://127.0.0.1:5000"

Tests:
The project includes a test.py file for testing both endpoints for a few cases:
1. /IptoGeoInfo/[some legal IP address] : returns the geoInfo as requested.
2. /IpToGeoInfo/[some ilegal IP address] : returns "ErrorName: "IP not legal!" "
3. /CountryIPs/[some legal Country ID] : returns a list of all IPs ranges of the given country
4. /CountryIPs/[some ilegall Country ID] : return "ErrorName: "Country not found!" "

for running tests, run (from the projectr directory) 
'python3.10 test.py' 
after deployong server.



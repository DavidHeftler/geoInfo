import csv
import os
import sys
from collections import defaultdict
from ipConversion import intToIp
DB = os.path.join(sys.path[0], "resources/IP2LOCATION-LITE-DB1.CSV")

def defaultValue():
    return []

IPsInfo = []
IPsByCountry = defaultdict(defaultValue)


def loadIpData():
    file = open(DB, 'r')
    reader = csv.reader(file)
    for row in reader:
        from_, to, ID, name = int(row[0]), int(row[1]), row[2], row[3]
        if row[2] != "-":
            IPsInfo.append(((from_, to), (ID, name)))
            IPsByCountry[ID].append(intToIp(from_) + ' - ' + intToIp(to))
        else:
            IPsInfo.append(((from_, to), ("None", "None")))
    file.close()



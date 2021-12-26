import csv
import os
import sys

DB = os.path.join(sys.path[0], "resources/IP2LOCATION-LITE-DB1.CSV")

IPsInfo = []

def loadIpData():
    file = open(DB, 'r')
    reader = csv.reader(file)
    for row in reader:
        if row[2] == "-":
            continue
        begin, end, ID, name = int(row[0]), int(row[1]), row[2], row[3]
        IPsInfo.append(((begin, end), (ID, name)))
    file.close()




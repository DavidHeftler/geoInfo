import socket
import struct
import ipaddress

def ipToInt(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]


def intToIp(addr):
    return socket.inet_ntoa(struct.pack("!I", addr))



def ipIsLegal(address):
    try:
        ip = ipaddress.ip_address(address)
        return True
    except ValueError:
        return False

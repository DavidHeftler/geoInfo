import socket
import struct


def ipToInt(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]


def intToIp(addr):
    return socket.inet_ntoa(struct.pack("!I", addr))



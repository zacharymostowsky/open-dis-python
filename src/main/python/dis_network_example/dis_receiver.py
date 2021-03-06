#! /usr/bin/python


__author__ = "mcgredo"
__date__ = "$Jun 25, 2015 12:10:26 PM$"

import socket
import time
import sys


from dis_io.DataInputStream import DataInputStream
from dis_io.DataOutputStream import DataOutputStream


from distributed_interactive_simulation.dis7 import *
from distributed_interactive_simulation.RangeCoordinates import GPS
import distributed_interactive_simulation.PduFactory as pduFactory
import binascii

UDP_PORT = 3001

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
udpSocket.bind(("", UDP_PORT))
print("Created UDP socket {}".format(UDP_PORT))

while True:
    data, addr = udpSocket.recvfrom(1024) # buffer size is 1024 bytes
    #print("received message:{} {}".format(len(data), binascii.b2a_qp(data)))
    aPdu = pduFactory.createPdu(data);
    print("Pdu location is {} {} {}".format(aPdu.entityLocation.x, aPdu.entityLocation.y, aPdu.entityLocation.z))

if __name__ == "__main__":
    print("Hello World")

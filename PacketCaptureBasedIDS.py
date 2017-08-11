'''
Created on Aug 9, 2016
@author: Henry Wang

Creating a intrusion detection system. Sniff all of the IP packets using a raw socket.
Raw socket is a socket the sends and receives data in binary.
IDS read an IP packet and analyze the received packet in binary according to the IP protocol.

   IPHader format:

    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |Version|  IHL  |Type of Service|          Total Length         |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |         Identification        |Flags|      Fragment Offset    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |  Time to Live |    Protocol   |         Header Checksum       |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                       Source Address                          |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Destination Address                        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Options                    |    Padding    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

'''

import socket
import struct

#Create RAW socket and bind to (localhost, 0). recvfrom packet (header + playload), 
#parse IPheader then reutrn packet, receiveraddress, version, IHL, totallength, ID, protocol, sourceAddress, distinationAddress, playload for test analyze   

def PacketCaptureBasedIDSAnalyze():
    packet = None
    receiveraddress = ''
    version = ''
    IHL = ''
    totallength = ''
    ID = ''
    protocol = ''
    sourceAddress = ''
    distinationAddress = ''
    playload = ''

    
    return packet, receiveraddress, version, IHL, totallength, ID, protocol, sourceAddress, distinationAddress, playload  
    
#Create command line able to call above functions with given snedMessage.	  
if __name__ == '__main__':
    PacketCaptureBasedIDSAnalyze()

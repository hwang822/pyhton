'''
Created on Jul 14, 2016
@author: Henry Wang
   
'''

import socket
import struct
import os
import sys

#Create a ROW PACKET socket (host = 'localhost', port = 0, socket type = socket.SOCK_RAW) which will send a packet including ip_header(20 bytes) and sendMessage. The socket will bind to local HOST server = (HOST, 0). Using creted socket.sendto(sendMessage, server) to Local HOST server. return created socket.
#Receive a packet from the created socket of local host with IPheader + Message + Address.
#Unpacket IPHeader as below table.
'''
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
#return Version, IHL, Total Length, Identification, Protocol, Source Address, Destination Address, Message for filters

def PacketsCaptureFilter(sendMessage):
   version = ''
   IHL = ''
   totallength = ''
   ID = ''
   protocol = ''
   sourceAddr = ''
   distinationAddress = ''
   recMessage = ''

   return version, IHL, totallength, ID, protocol, sourceAddr, distinationAddress, messageRc  

#Create CaptureFilterVersion(message, versionFilter) to compare default version number (4) from IPHader:   
def CaptureFilterVersion(message, versionFilter):
   filterCompare = False

   return filterCompare

#Create CaptureFilterIHL(message, IHLFilter) to compare IHL (20) from IPHader:      
def CaptureFilterIHL(message, IHLFilter):
   filterCompare = False

   return filterCompare

#Create CaptureFilterTotallength(message, TotallengthFilter) to compare Totallength (20 + message size) from IPHader:   
def CaptureFilterTotallength(message, totallengthFilter):
   filterCompare = False

   return filterCompare

#Create CaptureFilterID(message, TotallengthFilter) to compare ID  from IPHader:      
def CaptureFilterID(message, IDFilter):
   filterCompare = False

   return filterCompare

#Create CaptureFilterProtocol(message, protocolFilter) to compare Protocol # from IPHader:
def CaptureFilterProtocol(message, protocolFilter):
   filterCompare = False

   return filterCompare

#Create CaptureFilterSourceAddr(message, sourceAddrFilter) to compare SourceAddr (defaut 'localhost' ) from IPHader:
def CaptureFiltersSourceAddr(message, sourceAddrFilter):
   filterCompare = False

   return filterCompare

#Create CaptureFilterdistinationAddress(message, distinationAddressFilter) to compare distinationAddress (defaut 'localhost' ) from IPHader:   
def CaptureFiltersDistinationAddress(message, distinationAddressFilter):
   filterCompare = False

   return filterCompare

#Create CaptureFilterMessage(message, messageAddressFilter) to compare message (defaut 'localhost' ) from IPHader:      
def CaptureFiltersMessage(message, messageFilter):
   filterCompare = False

   return filterCompare

#Create command line able to call above functions with given snedMessage.	  
if __name__ == '__main__':
    sendMessage = sys.argv[1]	
    PacketsCaptureFilter(sendMessage)